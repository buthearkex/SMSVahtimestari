package smsVahtimestari

import smsVahtimestari.commands.Oven

import smsVahtimestari.commands.Car

import smsVahtimestari.commands.Sauna

import smsVahtimestari.commands.Electricity

import smsVahtimestari.commands.AirConditioning

import smsVahtimestari.commands.Help

import smsVahtimestari.commands.DoorGuard

object Commands extends Enumeration {
	val HELP = Help
	val SAUNA = Sauna
	val OVEN = Oven
	val CAR = Car
	val AC = AirConditioning
	val EL = Electricity
	val DG = DoorGuard
}