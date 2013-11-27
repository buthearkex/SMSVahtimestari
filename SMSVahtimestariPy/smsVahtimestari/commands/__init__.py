import random
import datetime

class AirConditioning:

    def howManyParameters(self):
        return 1
    
    def __init__(self):
        self.isOn = False
        self.currentTemperature = 25
    
    def status(self):
        temp = "Asunnon lämpötila on nyt " + str(self.currentTemperature)
        if (self.isOn):
            temp += " ja ilmastointi on päällä"
        else:
            temp += " ja ilmastointi ei ole päällä"
        return temp
    
    def turnOnOff(self, onOff):
        if (self.isOn and onOff):
            return "Ilmastointi on jo päällä" 
        elif (self.isOn): 
            self.isOn = False 
            return "Ilmastointi sammutetaan"
        elif (onOff):
            self.isOn = True
            return "Ilmastointi lämmitetään" 
        else:
            return "Ilmastointi ei ollut päällä"
    
    def __str__(self):
        return "ilmastointi"
        
class Car:

    def howManyParameters(self):
        return 2
    
    def __init__(self):
        self.heatingTimeMin = datetime.timedelta(minutes=15)
        self.currentTime = datetime.datetime.now()
        self.isOn = False    

    def turnOnOff(self, onOff):
        if (self.isOn and onOff):
            return "Auton lämmitys on jo päällä" 
        elif(self.isOn): 
            self.isOn = False 
            return "Auton lämmitys sammutetaan"  
        elif (onOff):
            self.isOn = True 
            return "Auton lämmitys lämmitetään" 
        else:
            return "Auton lämmitys ei ollut päällä" 

    def status(self):
        if (self.isOn):
            return "Auton lämmitys päällä"
        else:
            return "Auton lämmitys ei päällä"

    def setTimer(self, hours, minutes):
        year = self.currentTime.year
        month = self.currentTime.month
        day = self.currentTime.day
        diff = datetime.timedelta(self.currentTime, datetime.datetime(year, month, day, hours, minutes))
        realDiff = self.heatingTimeMin - diff
        if (realDiff < 0):
            return "Liian vähän aikaa, aloitetaan lämmitys nyt, valmista on... "
        else:
            return "Kelpaa, lämpenee valmiiksi kello " + str(hours) + ":" + str(minutes)
    
    def __str__(self):
        return "auto"


class DoorGuard:

    def howManyParameters(self):
        return 1
    
    def __init__(self):
        self.isOn = False

    def turnOnOff(self, onOff):
        if (self.isOn and onOff):
            return "Ovivahti on jo päällä" 
        elif (self.isOn): 
            self.isOn = False 
            return "Ovivahti sammutetaan" 
        elif (onOff):
            self.isOn = True 
            return "Ovivahti päälle"
        else:
            return "Ovivahti ei ollut päällä" 

    def status(self):
        if (self.isOn):
            return "Ovivahti päällä"
        else:
            return "Ovivahti pois päältä"

    def __str__(self):
        return "ovivahti"
        

class Electricity:

    def howManyParameters(self):
        return 0
    
    def __init__(self):
        self.elConsumption = random.randint(200, 1000)

    def status(self):
        return "Sähköä kuluu nyt " + str(self.elConsumption) + " W"

    def __str__(self):
        return "sahko"


class Help:

    def howManyParameters(self):
        return 0
    
    def status(self):
        return "Tässäpä sinulle ohjeet: \n" + "Sauna \n" + "Uuni \n" + "Auto \n" + "Lämmitys \n" + "Sähkö \n" + "Ovivahti"

    def __str__(self):
        return "apua"

    
class Sauna:

    def howManyParameters(self):
        return 3
    
    def __init__(self):
        self.heatingTimeMin = datetime.timedelta(minutes = 45)
        self.currentTemperature = 25
        self.currentTime = datetime.datetime.now()
        self.isOn = False
        self.warmAt = 0,0
    
    def setTemperature(self, temperature):
        if (temperature > 120 and temperature < 40):
            return "Anna luku väliltä 40-120"
        else:
            return "Sauna lämpötilassa " + str(temperature) + " klo " + "XXXXXX"

    def getCurrentTemperature(self):
        return self.currentTemperature

    def setTimer(self, hours, minutes):
        year = self.currentTime.year
        month = self.currentTime.month
        day = self.currentTime.day
        diff = datetime.timedelta(self.currentTime, datetime.datetime(year, month, day, hours, minutes))
        realDiff = self.heatingTimeMin - diff
        if (realDiff < 0):
            return "Sauna ei ehdi lämmetä ajoissa, mutta lämmitys aloitetaan."
        else:
            self.isOn = True
            warmAt = hours, minutes
            return "Mihin lämpötilaan?"


    def turnOnOff(self, onOff):
        if (self.isOn and onOff):
            return "kiuas on jo päällä" 
        elif (self.isOn): 
            self.isOn = False 
            return "kiuas sammutetaan"
        elif (onOff): 
            self.isOn = True 
            return "kiuas lämmitetään" 
        else:
            return "kiuas ei ollut päällä" 

    def status(self):
        if(self.isOn):
            return "Sauna on lämpenemässä ja sen lämpö on nyt " + str(self.currentTemperature)
        else:
            return "Sauna ei ole päällä ja sen lämpö on nyt " + str(self.currentTemperature)

    def __str__(self):
        return "sauna"
    
class Oven:

    def howManyParameters(self):
        return 3
    
    def __init__(self):
        self.heatingTimeMin = datetime.timedelta(minutes = 45)
        self.currentTemperature = 25
        self.currentTime = datetime.datetime.now()
        self.isOn = False
    
    def setTemperature(self, temperature):
        if (temperature > 120 and temperature < 20):
            return "Luku ei kelpaa. Anna lämpötila 300-20 väliltä"
        else:
            return "Kelpaa, lämpenee " + str(temperature)

    def getCurrentTemperature(self):
        return self.currentTemperature

    def setTimer(self, hours, minutes):
        year = self.currentTime.year
        month = self.currentTime.month
        day = self.currentTime.day
        diff = datetime.timedelta(self.currentTime, datetime.datetime(year, month, day, hours, minutes))
        realDiff = self.heatingTimeMin - diff
        if (realDiff < 0):
            return "Liian vähän aikaa, aloitetaan lämmitys nyt, valmista on... "
        else:
            return "Kelpaa, lämpenee valmiiksi kello " + str(hours) + ":" + str(minutes)

    def turnOnOff(self, onOff):
        if (self.isOn and onOff):
            return "uuni on jo päällä" 
        elif (self.isOn): 
            self.isOn = False 
            return "uuni sammutetaan"
        elif (onOff): 
            self.isOn = True 
            return "uuni lämmitetään" 
        else:
            return "uuni ei ollut päällä" 

    def status(self):
        if(self.isOn):
            return "uuni on lämpenemässä ja sen lämpö on nyt " + str(self.currentTemperature)
        else:
            return "uuni ei ole päällä ja sen lämpö on nyt " + str(self.currentTemperature)

    def __str__(self):
        return "uuni"