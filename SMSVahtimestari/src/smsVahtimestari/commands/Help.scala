package smsVahtimestari.commands

import smsVahtimestari.StatusTrait

object Help extends StatusTrait {
	def status(): String = {
		"Tässäpä sinulle ohjeet: \n" +
			"Sauna \n" +
			" \n" +
			" \n" +
			" \n" +
			" \n" +
			" \n" +
			" \n" +
			" \n" +
			" \n" +
			" \n"
	}

	def toString = "apua"
}