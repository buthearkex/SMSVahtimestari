package smsVahtimestari.commands

import smsVahtimestari.OnOffTrait

object DoorGuard extends OnOffTrait {

	def turnOnOff(status: Boolean): String = ???

	def status(): String = ???

	def toString = "ovivahti"
}