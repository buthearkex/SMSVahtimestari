package smsVahtimestari

import smsVahtimestari.commands.Oven

import smsVahtimestari.commands.Car

import smsVahtimestari.commands.Sauna

import smsVahtimestari.commands.Electricity

import smsVahtimestari.commands.AirConditioning

import smsVahtimestari.commands.Help

import smsVahtimestari.commands.DoorGuard

object Commands extends Enumeration {
	val HELP = ("apua", Help)
	val SAUNA = ("sauna", Sauna)
	val OVEN = ("uuni", Oven)
	val CAR = ("auto", Car)
	val AC = ("lämmitys", AirConditioning)
	val EL = ("sähkö", Electricity)
	val DG = ("ovivahti", DoorGuard)
}