package smsVahtimestari
import Commands._
import smsVahtimestari.commands.Sauna

object CommandInterpreter {
	var topic = None
	
	def interpret (msg: String): String = {
		msg match{
			case SAUNA => {
				topic = SAUNA
				Sauna.status()
			}
		}
	}
}