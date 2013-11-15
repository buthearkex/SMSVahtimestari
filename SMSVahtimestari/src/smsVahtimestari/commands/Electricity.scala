package smsVahtimestari.commands

import smsVahtimestari.StatusTrait

object Electricity extends StatusTrait {
	val rnd = new Random()
	val elConsumption = rnd.nextInt(200, 10000)

	def status(): String = "Sähköä kuluu nyt "+ elConsumption.toString +"Wattia"

	def toString = "sähkö"
}