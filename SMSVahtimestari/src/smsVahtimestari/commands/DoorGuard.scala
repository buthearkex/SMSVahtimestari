package smsVahtimestari.commands

import smsVahtimestari.OnOffTrait

object DoorGuard extends OnOffTrait {
	var isOn = false

	def turnOnOff(status: Boolean): String = {
		if(isOn && status) "Ovivahti on jo päällä" 
		else if(isOn) "Ovivahti sammutetaan" isOn = false 
		else if(status)"Ovivahti päälle" isOn = true
		else "Ovivahti ei ollut päällä" 
	}

	def status(): String = {
		if(isOn) "Ovivahti päällä"
		else "Ovivahti pois päältä"
	}

	def toString = "ovivahti"
}