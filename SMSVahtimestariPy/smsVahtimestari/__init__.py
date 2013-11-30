import string
import sys
import threading
import uuid

from smsVahtimestari.commands import *
from smsVahtimestari.smsMocks import *


class CommandInterpreter:
    # Static variables to be used as flags with methods.
    POSITIVE = str(uuid.uuid4())
    NEGATIVE = str(uuid.uuid4())
    RESET = str(uuid.uuid4())
    TIME = str(uuid.uuid4())
    TEMPERATURE = str(uuid.uuid4())
    
    # Static lists of possible commands.
    onOptions = ["päälle", "k", "kyllä", "joo"]
    offOptions = ["sammuta", "e", "ei", "pois", "älä"]
    resetCommands = ["lopeta", "palaa", "alkuun"]
    
    
    def __init__(self):
        self.topic = ""
        self.dialogueIsOn = False
        self.activeTopic = None
        self.questionNumber = 0
    
    def commandGiven(self, wordList, case):
        '''
        Check if command given was positive, negative or reset command depening on case.
        Possible cases are POSITIVE, NEGATIVE and RESET (static variables in CommandInterpreter).
        '''
        comparable = []
        if case == CommandInterpreter.POSITIVE:
            comparable = CommandInterpreter.onOptions
        elif case == CommandInterpreter.NEGATIVE:
            comparable = CommandInterpreter.offOptions
        elif case == CommandInterpreter.RESET:
            comparable = CommandInterpreter.resetCommands
        return len(set(comparable) & set(wordList)) > 0

    def typo(self):
        return """Viestiä ei ymmärretty. Tarkista muotoilu seuraavista esimerkeistä
  *apua* *kyllä* *ei* *alkuun* | aika *12.15* | lämpö *120*"""
    def isMessageUnderstood(self, wordList, case=0):
        if case == 0:
            return (self.commandGiven(wordList, CommandInterpreter.POSITIVE) or 
                    self.commandGiven(wordList, CommandInterpreter.RESET) or 
                    self.commandGiven(wordList, CommandInterpreter.NEGATIVE))
        else:
            for word in wordList:
                if word.isdigit(): 
                    return (int(word) < (2400 if case == CommandInterpreter.TIME else 301) and
                            int(word) > (-1 if case == CommandInterpreter.TIME else 30))
                elif case == CommandInterpreter.TIME:
                    others = word.split(":")
                    if len(others) != 2:
                        others = word.split(".")
                    if len(others) == 2 and self.isTime(others):
                        return True
            return False
    
    def isTime(self, num):
        return (num[0].isdigit() and int(num[0]) < 24) and (num[1].isdigit() and int(num[1]) < 60)

    def giveTopic(self, wordList):
        commandToCall = None
        for cmd in SMSVahtimestari.commands:
            if (str(cmd) in wordList):
                commandToCall = cmd
        self.activeTopic = commandToCall

    def giveTime(self, wordList):
        for word in wordList:
            if word.isdigit():
                if len(str(word)) < 4:
                    if len(str(word)) == 3:
                        return [int(word[:1]), int(word[1:3])]
                    elif len(str(word)) == 2:
                        return [0, int(word)]
                    else:
                        return [0, int(word)]
                else:
                    return [int(word[:2]), int(word[2:4])]
            else:
                others = word.split(":")
                if len(others) != 2:
                    others = word.split(".")
                if len(others) == 2:
                    return others

    def giveTemperature(self, wordList):
        for word in wordList:
            if word.isdigit():
                return int(word)

    def resetToStartingPoint(self):
        self.activeTopic = None
        self.questionNumber = 0

    def activeTopicHasNextQuestion(self):
        if self.questionNumber <= self.activeTopic.howManyParameters():
            return True
        return False

    
    def interpret(self, msg):
        '''
        saa käyttäjän viestin sellaisenaan ilman aiempia muokkauksia
        pyörittää dialogin logiikkaa = controller
        palauttaa dialogin toisen puolen takaisinpäin
        '''
        stringToReturn = ""
        willReset = False
        willTryToShortCut = False

        # alkutilanne
        # prosessoi viestin osiin ja yhtenäistaa muotoilun
        wordList = msg.split(' ')
        for idx, word in enumerate(wordList):
            wordList[idx] = word.lower().strip()

        # starting point
        if self.activeTopic is None:
            # hommaa actiivisen topikin
            self.giveTopic(wordList)
            if self.activeTopic is None:
                stringToReturn = self.typo()
            else:
                if self.activeTopic.howManyParameters() > 0 and len(wordList) == self.activeTopic.howManyParameters()+1:#+1 is for topic name
                    willTryToShortCut = True
                    if len(wordList) > 1:
                        laitetaanPaalle = self.commandGiven(wordList, CommandInterpreter.POSITIVE)
                        stringToReturn = self.activeTopic.turnOnOff(laitetaanPaalle)
                    if len(wordList) > 2:
                        aika = self.giveTime(wordList)
                        stringToReturn = self.activeTopic.setTimer(aika[0], aika[1])
                    if len(wordList) > 3:
                        lampotila = self.giveTemperature(wordList)
                        stringToReturn = self.activeTopic.setTemperature(lampotila)

                    #reseting
                    self.resetToStartingPoint()

        # "lopeta" command is given
        if self.commandGiven(wordList, CommandInterpreter.RESET):
            self.resetToStartingPoint()
            stringToReturn = "Palattiin alkuun."

        # topic is selected
        if self.activeTopic is not None and not willTryToShortCut:
            if self.activeTopicHasNextQuestion(): 
                # kysytään seuraavat kysymykset tässä järjestyksessä
                # status
                if self.questionNumber == 0:
                    stringToReturn = self.activeTopic.status()
                # on/off
                elif self.questionNumber == 1:
                    if self.isMessageUnderstood(wordList):
                        laitetaanPaalle = self.commandGiven(wordList, CommandInterpreter.POSITIVE)
                        stringToReturn = self.activeTopic.turnOnOff(laitetaanPaalle)
                        if not laitetaanPaalle:#no answer
                            willReset = True
                    else:  # was not understood
                        stringToReturn = self.typo()
                        self.questionNumber -= 1
                # timer
                elif self.questionNumber == 2:
                    if self.isMessageUnderstood(wordList, CommandInterpreter.TIME):
                        aika = self.giveTime(wordList)
                        stringToReturn = self.activeTopic.setTimer(aika[0], aika[1])
                    else:  # was not understood
                        stringToReturn = self.typo()
                        self.questionNumber -= 1
                # temperature
                elif self.questionNumber == 3:
                    if self.isMessageUnderstood(wordList, CommandInterpreter.TEMPERATURE):
                        lampotila = self.giveTemperature(wordList)
                        stringToReturn = self.activeTopic.setTemperature(lampotila)
                    else:  # was not understood
                        stringToReturn = self.typo()
                        self.questionNumber -= 1
                else:
                    print(self.questionNumber)
                self.questionNumber += 1
            
            if willReset or (self.activeTopic is not None and not self.activeTopicHasNextQuestion()):
                self.resetToStartingPoint()

        return stringToReturn

class SMSVahtimestari:
    commands = [Help(), Sauna(), Oven(), Car(), AirConditioning(), DoorGuard()]
    commandInterpreter = CommandInterpreter()

    def __init__(self):
        self.number = str(sys.argv)
        self.receiver = SMSReceiver(self.handleMessage, self.number)
        self.sender = SMSSender(self.number)
        self.receiver.listen()

    def handleMessage(self, msg):
        self.sender.send(SMSVahtimestari.commandInterpreter.interpret(msg))
        self.receiver.listen()

if __name__ == "__main__":
    SMSVahtimestari()

