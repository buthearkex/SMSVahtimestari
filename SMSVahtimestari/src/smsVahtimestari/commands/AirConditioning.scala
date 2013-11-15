package smsVahtimestari.commands

import smsVahtimestari.OnOffTrait

object AirConditioning extends OnOffTrait {

	private var isOn = false
	val currtentTemperature = 25

	def status(): String = {
		val temp = "Asunnon lämpötila on nyt " + currtentTemperature.toString()
		if(isOn) temp += " ja ilmastointi on päällä"
		else temp += " ja ilmastointi ei ole päällä"

	def turnOnOff(status: Boolean): String = {
		if(isOn && status) "Ilmastointi on jo päällä" 
		else if(isOn) "Ilmastointi sammutetaan" isOn = false 
		else if(status)"Ilmastointi lämmitetään" isOn = true
		else "Ilmastointi ei ollut päällä" 
	}
	
	def toString = "lämmitys"
}
