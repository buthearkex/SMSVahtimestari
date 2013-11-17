package smsVahtimestari.commands

import smsVahtimestari.TimerTrait

object Car extends TimerTrait {
	val heatingTimeMin = 15
	val clock = new Time()//MITES VIDUUS TÄS SCALAAS TEHDÄÄ OLIOIIT???
	var isOn = false	

	def turnOnOff(status: Boolean): String = {
		if(isOn && status) "Auton lämmitys on jo päällä" 
		else if(isOn){ 
			isOn = false 
			"Auton lämmitys sammutetaan"  
		}
		else if(status){ 
			isOn = true 
			"Auton lämmitys lämmitetään" 
		}
		else "Auton lämmitys ei ollut päällä" 
	}

	def status(): String = {
		if(isOn) "Auton lämmitys päällä"
		else "Auton lämmitys ei päällä"
	}

	def setTimer(time: Int): String = {
		if(clock.getMinutesTo(time) > heatingTimeMin)"Liian vähän aikaa, aloitetaan lämmitys nyt, valmista on... "
		else "Kelpaa, lämpenee valmiiksi kello " + time.toString
	}
	
	override def toString = "auto"
}