package smsVahtimestari

import smsMocks._
import Commands._

object SMSVahtimestari extends App{
	def handleMessage(msg: String) {
		sender.send(CommandInterpreter.interpret(msg))
	}
	
	val receiver: SMSReceiver = new SMSReceiver(handleMessage)
	val sender: SMSSender = new SMSSender
	
	println("SMSVahtimestari on p��ll�. L�het� k�sky " + Help + " mik�li tarvitset apua k�yt�ss�.")
}