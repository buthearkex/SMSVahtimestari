package smsVahtimestari.commands

import smsVahtimestari.commands._
import smsVahtimestari.TemperatureTrait

object Sauna extends TemperatureTrait {
	val heatingTimeMin = 45
	val currtentTemperature = 25
	val clock: Time = new Time()//MITES VIDUUS TÄS SCALAAS TEHDÄÄ OLIOIIT???
	
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
		if(clock.getMinutesTo(time)){
			"Liian vähän aikaa, aloitetaan lämmitys nyt, valmista on... "
		}
		else {
			"Kelpaa, lämpenee valmiiksi kello " + time.toString
		}
	}

	def turnOnOff(status: Boolean): String = ???

	def status(): String = ???

	def toString = "sauna"
}