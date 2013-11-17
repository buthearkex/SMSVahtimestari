package smsMocks

import java.io.InputStream
import scala.io.Codec

class SMSReceiver(val callback: String => Unit) {
	
//	def inputStreamToString(is: InputStream) = {
//		scala.io.Source.fromInputStream(is)(Codec.UTF8).getLines().mkString("\n")
//	}
	
	def listen {
//		callback(inputStreamToString(System.in))
		callback(readLine())
	}
}