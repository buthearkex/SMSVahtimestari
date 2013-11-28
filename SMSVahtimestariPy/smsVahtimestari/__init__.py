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
        elif "sammuta" in wordList or "pois" in wordList:
            return False
        else:
            return False

    def isFinished(self, wordList):
        #mystinen logiikka
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

    def giveHours(self, msg):
        #mystinen logiikka
        return 20

    def giveMinutes(self, msg):
        #mystinen logiikka
        return 20

    def giveTemperature(self, msg):
        #mystinen logiikka
        return 80


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
        palautettavaString = ""

        #alkutilanne
        #prosessoi viestin osiin ja yhtenäistaa muotoilun
        wordList = msg.split(' ')
        for idx, word in enumerate(wordList):
            word.lower()
            word.strip()
            wordList[idx] = word
        if self.activeTopic is None:
            #hommaa actiivisen topikin
            self.giveTopic(wordList)

        if self.activeTopic is not None:
            if self.activeTopicHasNextQuestion(): 
                #kysytään seuraavat kysymykset tässä järjestyksessä
                #status
                if self.questionNumber == 0:
                    print("***status")
                    palautettavaString = self.activeTopic.status()
                #on/off
                elif self.questionNumber == 1:
                    print("***on/off")
                    laitetaanPaalle = self.isPositive(wordList)#(True tai False)
                    palautettavaString = self.activeTopic.turnOnOff(laitetaanPaalle)
                #timer
                elif self.questionNumber == 2:
                    print("***timer")
                    tunnit = self.giveHours(wordList)
                    minuutit = self.giveMinutes(wordList)
                    palautettavaString = self.activeTopic.setTimer(tunnit, minuutit)
                #temperature
                elif self.questionNumber == 3:
                    print("***temperature")
                    lampotila = self.giveTemperature(wordList)
                    palautettavaString = self.activeTopic.setTemperature(lampotila)
                else:
                    print("***tänne ei pitäisi päätyä")
                    print(self.questionNumber)
                self.questionNumber += 1
            
            #ei toteutettu elsellä, koska muuten tulisi tarpeeton syötepyyntö käyttäjälle
            if not self.activeTopicHasNextQuestion():
                print("***loppustatus - jätetty pois")
                #annetaan loppustatus
                #palautettavaString = self.activeTopic.status()
                
                #asia on käsitelty
                self.activeTopic = None
                self.questionNumber = 0
                print("***nyt dialogi on alkutilanteessa")

        #lopeta komento annettu tai asia on käsitelty
        if self.isFinished(wordList):
            self.activeTopic = None
            self.questionNumber = 0
            print("***nyt dialogi on alkutilanteessa")

        return palautettavaString

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

'''
    def vanhaInterpreterJaMuutakin():
        #prosessoi viestin osiin ja yhtenäistaa muotoilun
        wordList = msg.split(' ')
        for idx, word in enumerate(wordList):
            word.lower()
            word.strip()
            wordList[idx] = word
        #jos viestissa ja kaskyissa on jokin sama niin muutetaan comentoa cutsuttavaa
        commandToCall = None
        for cmd in SMSVahtimestari.commands:
            if (str(cmd) in wordList):
                commandToCall = cmd
#-------------------------------------------

        self.activeTopic = commandToCall
#-------------------------------------------
            # topikki on valittu
            elif self.stateLAITATASTAENUMI = 0 and self.activeTopic.howManyParameters() >= 0:
                self.activeTopic.status()
                #esitetään kysymys
                if self.isPositive():
                    stateLAITATASTAENUMI = 1

            # päälle pois valittu
            elif self.stateLAITATASTAENUMI = 1 and self.activeTopic.howManyParameters() >= 1:
                self.activeTopic.turnOnOff()
                #esitetään kysymys
                if self.answerWasGiven:

            # aika on valittu
            elif self.stateLAITATASTAENUMI = 2 and self.activeTopic.howManyParameters() >= 2:
                self.activeTopic.setTimer()
                #esitetään kysymys
                if self.answerWasGiven:

            # lämpö on valittu
            elif self.stateLAITATASTAENUMI = 3 and self.activeTopic.howManyParameters() >= 3:
                self.activeTopic.setTemperature()


        if (self.topic != str(commandToCall)):
            self.topic = str(commandToCall)
            self.activeTopic = commandToCall
            
            #ei enää alkutilanne

        if #ei enää alkutilanne
            return self.activeTopic.status()# laitetaanko päälle

        elif#

        if self.activeTopic.howManyParameters() < self.stateLAITATASTAENUMI:
#-------------------------------------------
        if self.dialogueIsOn:
                #tassa vaiheessa kaskee asian päälle jos paasee tanne asti
                return "dialogia: " + self.activeTopic.turnOnOff(True)
        else:
            #jos viestissa ja kaskyissa on jokin sama niin muutetaan comentoa cutsuttavaa
            #MUTTA EI SE SITÄ VOI TEHDÄ JOKA KERTA TAI MUUTEN EI TUU DIALOGIA
            commandToCall = None
            for cmd in SMSVahtimestari.commands:
                if (str(cmd) in wordList):
                    commandToCall = cmd

            #jos asiasanaa ei loytynyt listasta
            if (commandToCall == None):
                return SMSVahtimestari.commands[0].status()
            #kutsutaan kesken kaiken toista topikkia
            elif (self.topic != str(commandToCall)):
                self.topic = str(commandToCall)
                self.activeTopic = commandToCall
                return commandToCall.status()

            else:
                self.dialogueIsOn = True
'''
