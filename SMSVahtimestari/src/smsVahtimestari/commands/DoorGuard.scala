package smsVahtimestari.commands

import smsVahtimestari.OnOffTrait

object DoorGuard extends OnOffTrait {
	var isOn = false

	def turnOnOff(status: Boolean): String = {
		if(isOn && status) "Ovivahti on jo päällä" 
		else if(isOn){ 
			isOn = false 
			"Ovivahti sammutetaan" 
		}
		else if(status){ 
			isOn = true 
			"Ovivahti päälle"
		}
		else "Ovivahti ei ollut päällä" 
	}

	def status(): String = {
		if(isOn) "Ovivahti päällä"
		else "Ovivahti pois päältä"
	}

	override def toString = "ovivahti"
}