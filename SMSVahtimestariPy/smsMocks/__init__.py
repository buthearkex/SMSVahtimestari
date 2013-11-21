'''
Created on 18.11.2013

@author: Leinonen
'''

class SMSReceiver:
    
    def __init__(self, callback):
        self.callback = callback
    
    def listen(self):
        self.callback(input())

class SMSSender:
    
    def send(self, msg):
        print(msg)