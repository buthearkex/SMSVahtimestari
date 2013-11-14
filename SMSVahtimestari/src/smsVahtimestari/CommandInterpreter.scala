package smsVahtimestari
import Commands._

object CommandInterpreter {
	var topic: String = null

	def interpret (msg: String): String = {
		for(value <- Commands.values) {
			if(topic != value._1){
				topic = value._1
				value._2.status()
			}
		}
	}
}
