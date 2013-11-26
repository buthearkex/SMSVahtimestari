from smsMocks import *
from smsVahtimestari.commands import *


class CommandInterpreter:
    
    def __init__(self):
        self.topic = ""
        self.dialogueIsOn = False
        self.activeTopic = None
        self.stateLAITATASTAENUMI = 0

    def isPositive(self, msg):
        #prosessoi viestin osiin ja yhtenäistaa muotoilun
        wordList = msg.split(' ')
        for idx, word in enumerate(wordList):
            word.lower()
            word.strip()
            wordList[idx] = word
        #mystinen logiikka
        return True

    def giveTopic(self, msg):
        commandToCall = None
        for cmd in SMSVahtimestari.commands:
            if (str(cmd) in wordList):
                commandToCall = cmd


    def interpret(self, msg):
        #alkutilanne
        if activeTopic is None:
            #hommaa actiivinen topikki
        else:
            self.activeTopic.status()

            #tulkitaan msg

            self.activeTopic.turnOnOff()
            self.activeTopic.setTimer()

            #katsotaan että temp on hyvä
            temp = msg
            self.activeTopic.setTemperature(temp)


    def tassa on vaan roskakoodia():
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