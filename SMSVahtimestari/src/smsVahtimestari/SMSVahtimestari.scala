package smsVahtimestari

import smsMocks._
import Commands._

object SMSVahtimestari extends App {
	def handleMessage(msg: String) {
		sender.send(CommandInterpreter.interpret(msg))
		receiver.listen
	}

	val receiver: SMSReceiver = new SMSReceiver(handleMessage)
	val sender: SMSSender = new SMSSender

	println("SMSVahtimestari on päällä. Lähetä käsky " + HELP + " mikäli tarvitset apua käytässä.")

	receiver.listen
}