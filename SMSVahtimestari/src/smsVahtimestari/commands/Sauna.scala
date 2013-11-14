package smsVahtimestari.commands

import smsVahtimestari.TemperatureTrait

object Sauna extends TemperatureTrait {
	
	def setTemperature(temperature:Int):String = {
		//tutkitaan arvo
		if(temperature > 120 && temperature < 20) {
			"Luku ei kelpaa. Anna lämpötila 120-20 väliltä"
		}
		else{
			"Kelpaa"
		}
	}
}