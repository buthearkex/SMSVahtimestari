package smsVahtimestari.commands
import java.util.Random
import smsVahtimestari.StatusTrait

object Electricity extends StatusTrait {
	val rnd = new Random
	val elConsumption = rnd.nextInt(1000) + 200

	def status(): String = "Sähköä kuluu nyt "+ elConsumption.toString +"Wattia"

	override def toString = "sähkö"
}