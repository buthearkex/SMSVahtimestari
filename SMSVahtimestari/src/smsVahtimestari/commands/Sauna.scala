package smsVahtimestari.commands

import smsVahtimestari.commands._
import smsVahtimestari.TemperatureTrait

object Sauna extends TemperatureTrait {
	val heatingTimeMin = 45
	val currtentTemperature = 25
	val clock = new Time()//MITES VIDUUS TÄS SCALAAS TEHDÄÄ OLIOIIT???
	var isOn = false
	
	def setTemperature(temperature: Int): String = {
		//tutkitaan arvo
		if (temperature > 120 && temperature < 20) {
			"Luku ei kelpaa. Anna lämpötila 120-20 väliltä"
		} else {
			"Kelpaa, lämpenee " + temperature.toString
		}
	}

	def getCurrentTemperature(): Int = {
		currtentTemperature
	}

	def setTimer(time:Int):String = {
		if(clock.getMinutesTo(time) > heatingTimeMin)"Liian vähän aikaa, aloitetaan lämmitys nyt, valmista on... "
		else "Kelpaa, lämpenee valmiiksi kello " + time.toString
	}

	def turnOnOff(status: Boolean): String = {
		if(isOn && status) "kiuas on jo päällä" 
		else if(isOn){ 
			isOn = false 
			"kiuas sammutetaan"  
		}
		else if(status){ 
			isOn = true 
			"kiuas lämmitetään" 
		}
		else "kiuas ei ollut päällä" 
	}

	def status(): String = {
		if(isOn) "Sauna on lämpenemässä ja sen lämpö on nyt " + currtentTemperature.toString
		else "Sauna ei ole päällä ja sen lämpö on nyt " + currtentTemperature.toString
	}

	def toString = "sauna"
}