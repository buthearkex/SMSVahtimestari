package smsVahtimestari.commands

import smsVahtimestari.OnOffTrait

object AirConditioning extends OnOffTrait {

	private var isOn = false
	val currtentTemperature = 25

	def status(): String = {
		var temp = "Asunnon lämpötila on nyt " + currtentTemperature.toString()
		if(isOn) temp += " ja ilmastointi on päällä"
		else temp += " ja ilmastointi ei ole päällä"
		temp
	}

	def turnOnOff(status: Boolean): String = {
		if(isOn && status) "Ilmastointi on jo päällä" 
		else if(isOn){ 
			isOn = false 
			"Ilmastointi sammutetaan"} 
		else if(status){
			isOn = true
			"Ilmastointi lämmitetään" }
		else "Ilmastointi ei ollut päällä" 
	}
	
	override def toString = "lämmitys"
}
