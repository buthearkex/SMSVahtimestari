from smsMocks import *
from smsVahtimestari.commands import *


class CommandInterpreter:
    
    def __init__(self):
        self.topic = ""

    def interpret(self, msg):
        #prosessoi viestin osiin ja yhtenäistaa muotoilun
        wordList = msg.split(' ')
        for idx, word in enumerate(wordList):
            word.lower()
            word.strip()
            wordList[idx] = word

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
            return commandToCall.status()

        #varsinainen dialogi alkaa tasta
        else:
            #tassa vaiheessa kaskee saunan lampenemaan jos paasee tanne asti
            return "aasd" + Sauna().turnOnOff(True)

class SMSVahtimestari:
    commands = [Help(), Sauna(), Oven(), Car(), AirConditioning(), Electricity(), DoorGuard()]
    commandInterpreter = CommandInterpreter()

    def __init__(self):
        self.receiver = SMSReceiver(self.handleMessage)
        self.sender = SMSSender()
        print("SMSVahtimestari on päällä. Lähetä käsky " + str(SMSVahtimestari.commands[0]) + " mikäli tarvitset apua käytässä.\n")
        self.receiver.listen()

    def handleMessage(self, msg):
        self.sender.send(SMSVahtimestari.commandInterpreter.interpret(msg))
        self.receiver.listen()

if __name__ == "__main__":
    SMSVahtimestari()