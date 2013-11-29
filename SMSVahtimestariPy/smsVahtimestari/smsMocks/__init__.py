'''
Contains mocks for receiving and sending text messages.

@author: Leinonen
'''

class SMSReceiver:
    
    def __init__(self, callback, number):
        '''
        Mock for receiving text messages.
        Callback should be a function that can handle string-format messages.
        '''
        self.callback = callback
        self.numberToListen = number
    
    def listen(self):
        '''
        Starts listening for text messages and then sends the messages to callback given in init.
        '''
        self.callback(input())

class SMSSender:
    
    def __init__(self, number):
        '''
        Mock for sending text messages.
        '''
        self.numberToSendTo = number
    
    def send(self, msg):
        '''
        Sends the finished message to user.
        '''
        print(msg)