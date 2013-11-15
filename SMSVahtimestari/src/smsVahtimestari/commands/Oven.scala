package smsVahtimestari.commands

import smsVahtimestari.TemperatureTrait

object Oven extends TemperatureTrait {
	def setTemperature(temperature: Int): String = {
		val heatingTimeMin = 15
		val currtentTemperature = 25
		val clock = new Time()//MITES VIDUUS TÄS SCALAAS TEHDÄÄ OLIOIIT???
		var isOn = false
		//tutkitaan arvo
		if (temperature > 300 && temperature < 20) {
			"Luku ei kelpaa. Anna lämpötila 300-20 väliltä"
		} else {
			"Kelpaa, lämpenee " + temperature.toString
		}
	}

	def getCurrentTemperature(): Int = {
		25
	}

	def turnOnOff(status: Boolean): String = {
		if(isOn && status) "Uuni on jo päällä" 
		else if(isOn) "Uuni sammutetaan" isOn = false 
		else if(status)"Uuni lämmitetään" isOn = true
		else "Uuni ei ollut päällä" 
	}

	def status(): String = {
		if(isOn) "Uuni on lämpenemässä ja sen lämpö on nyt " + currtentTemperature.toString
		else "Uuni ei ole päällä ja sen lämpö on nyt " + currtentTemperature.toString
	}

	def setTimer(time: Int): String = {
		if(clock.getMinutesTo(time) > heatingTimeMin)"Liian vähän aikaa, aloitetaan lämmitys nyt, valmista on... "
		else "Kelpaa, lämpenee valmiiksi kello " + time.toString
	}

	def toString = "uuni"
}