package smsVahtimestari.commands

import smsVahtimestari.StatusTrait

object Help extends StatusTrait {
	def status():String = {
		"Tässäpä sinulle ohjeet: \n"+
		"Sauna \n" +
		"Uuni \n" +
		"Auto \n" +
		"Lämmitys \n" +
		"Sähkö \n" +
		"Ovivahti \n" +
		" \n" +
		" \n" +
		" \n" +
		" \n" 
	}

	def toString = "apua"
}