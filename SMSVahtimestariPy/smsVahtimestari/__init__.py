import uuid

from smsMocks import *
from smsVahtimestari.commands import *


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
        return "Kirjoittaisitko asiat edes oikein"

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
        print("***nyt dialogi on alkutilanteessa")

    def activeTopicHasNextQuestion(self):
        # print("tultiin tänne mutta miksi")
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

        # alkutilanne
        # prosessoi viestin osiin ja yhtenäistaa muotoilun
        wordList = msg.split(' ')
        for idx, word in enumerate(wordList):
            word.lower()
            word.strip()
            wordList[idx] = word

        # starting point
        if self.activeTopic is None:
            # hommaa actiivisen topikin
            if self.giveTopic(wordList) is None:
                stringToReturn = self.typo()

        # "lopeta" command is given
        if self.commandGiven(wordList, CommandInterpreter.RESET):
            self.resetToStartingPoint()
            stringToReturn = "Palattiin alkuun."

        # topic is selected
        if self.activeTopic is not None:
            if self.activeTopicHasNextQuestion(): 
                # kysytään seuraavat kysymykset tässä järjestyksessä
                # status
                if self.questionNumber == 0:
                    print("***status")
                    stringToReturn = self.activeTopic.status()
                # on/off
                elif self.questionNumber == 1:
                    print("***on/off")
                    if self.isMessageUnderstood(wordList):
                        laitetaanPaalle = self.commandGiven(wordList, CommandInterpreter.POSITIVE)
                        stringToReturn = self.activeTopic.turnOnOff(laitetaanPaalle)
                        if not laitetaanPaalle:
                            willReset = True
                    else:  # was not understood
                        stringToReturn = self.typo()
                        self.questionNumber -= 1
                # timer
                elif self.questionNumber == 2:
                    print("***timer")
                    if self.isMessageUnderstood(wordList, CommandInterpreter.TIME):
                        aika = self.giveTime(wordList)
                        stringToReturn = self.activeTopic.setTimer(aika[0], aika[1])
                    else:  # was not understood
                        stringToReturn = self.typo()
                        self.questionNumber -= 1
                # temperature
                elif self.questionNumber == 3:
                    print("***temperature")
                    if self.isMessageUnderstood(wordList, CommandInterpreter.TEMPERATURE):
                        print("tänne tultiin")
                        lampotila = self.giveTemperature(wordList)
                        stringToReturn = self.activeTopic.setTemperature(lampotila)
                    else: # was not understood
                        stringToReturn = self.typo()
                        self.questionNumber -= 1
                else:
                    print("***tänne ei pitäisi päätyä")
                    print(self.questionNumber)
                self.questionNumber += 1
            
            if willReset or (self.activeTopic is not None and not self.activeTopicHasNextQuestion()):
                print("***loppustatus - jätetty pois")
                self.resetToStartingPoint()
        return stringToReturn

class SMSVahtimestari:
    commands = [Help(), Sauna(), Oven(), Car(), AirConditioning(), DoorGuard()]
    commandInterpreter = CommandInterpreter()

    def __init__(self):
        self.receiver = SMSReceiver(self.handleMessage)
        self.sender = SMSSender()
        self.receiver.listen()

    def handleMessage(self, msg):
        self.sender.send(SMSVahtimestari.commandInterpreter.interpret(msg))
        self.receiver.listen()

if __name__ == "__main__":
    SMSVahtimestari()

