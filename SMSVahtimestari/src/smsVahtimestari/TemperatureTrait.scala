package smsVahtimestari

trait TemperatureTrait extends TimerTrait{

  def setTemperature(temperature:Int):String
  def getCurrentTemperature(): Int
}
