package smsVahtimestari

import smsMocks._
import Commands._

object SMSVahtimestari extends App {
	def handleMessage(msg: String) {
		sender.send(CommandInterpreter.interpret(msg))
		receiver.listen
	}

	val receiver = new SMSReceiver(handleMessage)
	val sender = new SMSSender

	println("SMSVahtimestari on päällä. Lähetä käsky " + commands.Help + " mikäli tarvitset apua käytässä.")

	receiver.listen
}