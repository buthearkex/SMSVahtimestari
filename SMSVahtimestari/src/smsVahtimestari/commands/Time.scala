import java.util.Calendar
import java.text.SimpleDateFormat

object Time{
	def getMinutesTo(futureTimeInt: Int): Int = {
		var futureTime = futureTimeInt.toString
		val currentTime = getCurrentTime
		val currentTimeChars = currentTime.split("")
		val futureTimeChars = futureTime.split("")
		
		var mins = 0
		val currentMins = (currentTimeChars(2) + currentTimeChars(3)).toInt
		val futureMins = (futureTimeChars(2) + futureTimeChars(3)).toInt
		mins = futureMins - currentMins 

		var hours = 0
		val currentHours = (currentTimeChars(0) + currentTimeChars(1)).toInt
		val futureHours = (futureTimeChars(0) + futureTimeChars(1)).toInt
		hours = futureHours - currentHours

		mins += hours*60
		
		return mins
	}
  
	def getCurrentTime: String = {
		val today = Calendar.getInstance().getTime()
		val timeFormat = new SimpleDateFormat("HHmm")
		val time = timeFormat.format(today)
		return "" + time
	}
}