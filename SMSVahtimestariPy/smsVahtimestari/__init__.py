from smsMocks import *
from smsVahtimestari.commands import *

class SMSVahtimestari():
    commands = [Help(), Sauna(), Oven(), Car(), AirConditioning(), Electricity(), DoorGuard()]
    commandInterpreter = SMSVahtimestari.CommandInterpreter()

    def __init__(self):
        self.receiver = SMSReceiver(self.handleMessage)
        self.sender = SMSSender()
        print("SMSVahtimestari on päällä. Lähetä käsky " + SMSVahtimestari.commands[0] + " mikäli tarvitset apua käytässä.\n")
        self.receiver.listen()

    def handleMessage(self, msg):
        self.sender.send(SMSVahtimestari.commandInterpreter.interpret(msg))
        self.receiver.listen()

class CommandInterpreter():
    
    def __init__(self):
        self.topic = ""

    def interpret(self, msg):
        wordList = msg.split(' ').map(_.toLowerCase.trim)
        commandToCall = None
        for cmd in SMSVahtimestari.commands:
            if (wordList.exists(_ == cmd.toString)):
                commandToCall = cmd
        if (commandToCall == None):
            SMSVahtimestari.commands[0].status()
        elif (self.topic != commandToCall.toString):
            self.topic = commandToCall.toString
            commandToCall.status()
        else:
            "asd"

if __name__ == "__main__":
    SMSVahtimestari()