package smsVahtimestari.commands

import smsVahtimestari.TimerTrait

object Car extends TimerTrait {

	def status(): String = ???

	def turnOnOff(status: Boolean): String = ???

	def setTimer(time: Int): String = ???
	
	def toString = "auto"
}