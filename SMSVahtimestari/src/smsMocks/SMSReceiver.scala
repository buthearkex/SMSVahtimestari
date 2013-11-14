package smsMocks

class SMSReceiver(val callback: String => Unit) {
	
	def listen {
		callback(readLine())
	}
}