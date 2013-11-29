from smsMocks import *
from smsVahtimestari.commands import *


class CommandInterpreter:
    
    def __init__(self):
        self.topic = ""
        self.dialogueIsOn = False
        self.activeTopic = None
        self.questionNumber = 0

    def isPositive(self, wordList):
        if "päälle" in wordList or "k" in wordList or "kyllä" in wordList or "joo" in wordList:
            return True
        return False

    def isNegative(self, wordList):
        if "sammuta" in wordList or "ei" in wordList or "pois" in wordList or "älä" in wordList or "no" in wordList:
            return True
        return False

    def resetCommandWasGiven(self, wordList):
        if "lopeta" in wordList  or "palaa" in wordList or "alkuun" in wordList:
            return True
        else:
            return False

    def giveAllert(self):
        return "Kirjoittaisitko asiat edes oikein"

    def isMessageUnderstood(self, wordList):
        if self.isPositive(wordList) or self.resetCommandWasGiven(wordList) or self.isNegative(wordList):
            return True
        return False

    def isMessageUnderstoodAsTime(self, wordList):
        for word in wordList:
            if word.isdigit() and (int(word) < 2400): 
                return True
            else:
                others = word.split(":")
                if len(others) != 2:
                    others = word.split(".")
                if len(others) == 2 and (others[0].isdigit() and int(others[0]) < 24) and (others[1].isdigit() and int(others[1]) < 60):
                    return True
        return False
    
    def isMessageUnderstoodAsTemperature(self, wordList):
        for word in wordList:
            if word.isdigit() and (int(word) <= 300):
                return True
        return False

    def giveTopic(self, wordList):
        #mystinen logiikka
        
        #jos viestissa ja kaskyissa on jokin sama niin muutetaan comentoa cutsuttavaa
        commandToCall = None
        for cmd in SMSVahtimestari.commands:
            if (str(cmd) in wordList):
                commandToCall = cmd
        #self.activeTopic = Sauna()
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
        #print("tultiin tänne mutta miksi")
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

        #alkutilanne
        #prosessoi viestin osiin ja yhtenäistaa muotoilun
        wordList = msg.split(' ')
        for idx, word in enumerate(wordList):
            word.lower()
            word.strip()
            wordList[idx] = word

        #starting point
        if self.activeTopic is None:
            #hommaa actiivisen topikin
            if self.giveTopic(wordList) is None:
                stringToReturn = self.giveAllert()

        #"lopeta" command is given
        if self.resetCommandWasGiven(wordList):
            self.resetToStartingPoint()
            stringToReturn = "Palattiin alkuun."

        #topic is selected
        if self.activeTopic is not None:
            if self.activeTopicHasNextQuestion(): 
                #kysytään seuraavat kysymykset tässä järjestyksessä
                #status
                if self.questionNumber == 0:
                    print("***status")
                    stringToReturn = self.activeTopic.status()
                #on/off
                elif self.questionNumber == 1:
                    print("***on/off")
                    if self.isMessageUnderstood(wordList):
                        laitetaanPaalle = self.isPositive(wordList)#gives boolean
                        stringToReturn = self.activeTopic.turnOnOff(laitetaanPaalle)
                        if not laitetaanPaalle:
                            willReset = True
                    else:#was not understood
                        stringToReturn = self.giveAllert()
                        self.questionNumber -= 1
                #timer
                elif self.questionNumber == 2:
                    print("***timer")
                    if self.isMessageUnderstoodAsTime(wordList):
                        aika = self.giveTime(wordList)
                        stringToReturn = self.activeTopic.setTimer(aika[0], aika[1])
                    else:#was not understood
                        stringToReturn = self.giveAllert()
                        self.questionNumber -= 1
                #temperature
                elif self.questionNumber == 3:
                    print("***temperature")
                    lampotila = self.giveTemperature(wordList)
                    stringToReturn = self.activeTopic.setTemperature(lampotila)
                else:
                    print("***tänne ei pitäisi päätyä")
                    print(self.questionNumber)
                self.questionNumber += 1
            
            #ei toteutettu elsellä, koska muuten tulisi tarpeeton syötepyyntö käyttäjälle
            if willReset or (self.activeTopic is not None and not self.activeTopicHasNextQuestion()):
                print("***loppustatus - jätetty pois")
                #annetaan loppustatus
                #stringToReturn = self.activeTopic.status()
                
                #asia on käsitelty
                self.resetToStartingPoint()

        #lopeta komento annettu tai asia on käsitelty
        #if self.resetCommandWasGiven(wordList):
        #    self.resetToStartingPoint()

        return stringToReturn

class SMSVahtimestari:
    commands = [Help(), Sauna(), Oven(), Car(), AirConditioning(), DoorGuard()]
    commandInterpreter = CommandInterpreter()

    def __init__(self):
        self.receiver = SMSReceiver(self.handleMessage)
        self.sender = SMSSender()
        #ei printtiä  alkuun, koska tekstareissa ei silleen
        #print("SMSVahtimestari on päällä. Lähetä käsky " + str(SMSVahtimestari.commands[0]) + " mikäli tarvitset apua käytässä.\n")
        self.receiver.listen()

    def handleMessage(self, msg):
        self.sender.send(SMSVahtimestari.commandInterpreter.interpret(msg))
        self.receiver.listen()

if __name__ == "__main__":
    SMSVahtimestari()

