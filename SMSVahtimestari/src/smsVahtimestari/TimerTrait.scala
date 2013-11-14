package smsVahtimestari

trait TimerTrait {

   /**
   * time in form 0000, for example 12:34 is 1234
   * time tells when timer should run out, for example when the sauna should be warm
   */
  def setTimer(time:Int):String


}
