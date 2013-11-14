package smsVahtimestari.commands

import smsVahtimestari.TemperatureTrait

object Sauna extends TemperatureTrait {

	def setTemperature(temperature: Int): String = {
		//tutkitaan arvo
		if (temperature > 120 && temperature < 20) {
			"Luku ei kelpaa. Anna lämpötila 120-20 väliltä"
		} else {
			"Kelpaa, lämpenee " + temperature.toString
		}
	}

	def getCurrentTemperature(): Int = {
		25
	}

	def turnOnOff(status: Boolean): String = ???

	def status(): String = ???

	def setTimer(time: Int): String = ???

	def toString = "sauna"
}