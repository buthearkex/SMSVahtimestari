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
        
        if wordList = msg.split(' ')

    def giveTopic(self, wordList):
        #mystinen logiikka
        
        #jos viestissa ja kaskyissa on jokin sama niin muutetaan comentoa cutsuttavaa
        commandToCall = None
        for cmd in SMSVahtimestari.commands:
            if (str(cmd) in wordList):
                commandToCall = cmd
        #self.activeTopic = Sauna()
        self.activeTopic = commandToCall

    def giveHours(self, msg):
        #mystinen logiikka
        return 20

    def giveMinutes(self, msg):
        #mystinen logiikka
        return 20

    def giveTemperature(self, msg):
        #mystinen logiikka
        return 80

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
                        tunnit = self.giveHours(wordList)
                        minuutit = self.giveMinutes(wordList)
                        stringToReturn = self.activeTopic.setTimer(tunnit, minuutit)
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
    commands = [Help(), Sauna(), Oven(), Car(), AirConditioning(), Electricity(), DoorGuard()]
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

