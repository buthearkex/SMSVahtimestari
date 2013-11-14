package smsVahtimestari

trait TemperatureTrait extends timerTrait{

  def setTemperature(temperature:Int):String
  def getCurrentTemperature(): Int
}
