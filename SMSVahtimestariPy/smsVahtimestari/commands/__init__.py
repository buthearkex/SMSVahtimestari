import datetime
import random
import threading


class Sauna:

    def howManyParameters(self):
        return 3
    
    def __init__(self):
        self.heatingSpeed = 1.2
        self.currentTemperature = 25
        self.currentTime = datetime.datetime.now()
        self.isOn = False
        self.targetTimeHour = 0
        self.targetTimeMin = 0

    def giveHeatingTimeMin(self, targetTemperature):
        delta = targetTemperature - self.currentTemperature
        timeMin = int(delta / self.heatingSpeed)
        return timeMin
    
    def status(self):
        if(self.isOn):
            # when shutting down
            return "Sauna on päällä " + str(self.currentTemperature) + " °C. Sammuta komennolla *sammuta*."
        else:
            # when firing up
            return "Laitetaanko sauna päälle?"

    def turnOnOff(self, onOff):
        if (self.isOn and onOff):
            # firing up dialogue is going for second time by user
            return self.status() 
        elif (self.isOn): 
            # was on before
            self.isOn = False 
            return "Sauna sammutetaan."
        elif (onOff):
            # dialogue is going as normal
            self.isOn = True 
            return "Mihin aikaan sauna lämpimäksi?" 
        else:
            # when shutdown selected
            return "Saunaa ei lämmitetä." 

    def setTimer(self, hours, minutes):
        self.targetTimeHour = hours
        self.targetTimeMin = minutes
        return "Mihin lämpötilaan?"

    def setTemperature(self, temperature):
        formattedTime = datetime.datetime.strptime(str(self.targetTimeHour) + ":" + str(self.targetTimeMin), "%H:%M")
        diff = formattedTime - self.currentTime
        timeToHeat = self.giveHeatingTimeMin(temperature)
        diffMin = diff.seconds / 60
        # no time for heating
        print(diffMin) 
        print(timeToHeat)

        if (diffMin < timeToHeat):
            extraHours = 0
            while timeToHeat > 60:
                print("käytiin täällä")
                extraHours = 1
                timeToHeat - 60
            print(extraHours)
            warmAtStr = str(self.currentTime.hour + extraHours) + "." + str(int(self.currentTime.minute + diffMin))
            return "Sauna ei ehdi lämmetä ajoissa, mutta lämmitys aloitetaan. Valmis " + warmAtStr
        else:
            self.isOn = True
            minuteStr = str(self.targetTimeMin)
            if int(self.targetTimeMin) < 10:  # smoothly format minutes like 12.01 not 12.1
                minuteStr = "0" + str(self.targetTimeMin)
            warmAtStr = str(self.targetTimeHour) + "." + minuteStr
            return "Sauna lämpötilassa " + str(temperature) + " klo " + warmAtStr

    def getCurrentTemperature(self):
        return self.currentTemperature

    def __str__(self):
        return "sauna"
    
class Oven:

    def howManyParameters(self):
        return 3
    
    def __init__(self):
        self.heatingTimeMin = 45
        self.currentTemperature = 25
        self.currentTime = datetime.datetime.now()
        self.isOn = False
    
    def status(self):
        if(self.isOn):
           return "Sauna on päällä " + str(self.currentTemperature) + " °C."
        else:
            return "Laitetaanko uuni päälle?"
            # return "uuni ei ole päällä ja sen lämpö on nyt " + str(self.currentTemperature)
 
    def turnOnOff(self, onOff):
        if (self.isOn and onOff):
            return "uuni on jo päällä" 
        elif (self.isOn): 
            self.isOn = False 
            return "uuni sammutetaan"
        elif (onOff): 
            self.isOn = True 
            return "Mihin aikaan uuni lämpimäksi?" 
        else:
            return "uuni ei ollut päällä" 

    def getCurrentTemperature(self):
        return self.currentTemperature

    def setTimer(self, hours, minutes):
        timerTime = datetime.datetime.strptime(str(hours) + ":" + str(minutes), "%H:%M")
        diff = self.currentTime - timerTime
        realDiff = self.heatingTimeMin - int(diff.seconds / 60)
        if (realDiff < 0):
            return "Liian vähän aikaa, aloitetaan lämmitys nyt, valmista on... "
        else:
            return "Mihin lämpötilaan?"  # "Kelpaa, lämpenee valmiiksi kello " + str(hours) + ":" + str(minutes)

    def setTemperature(self, temperature):
        if (temperature > 120 and temperature < 20):
            return "Luku ei kelpaa. Anna lämpötila 300-20 väliltä"
        else:
            return "Kelpaa, lämpenee " + str(temperature)

    def __str__(self):
        return "uuni"

class Car:

    def howManyParameters(self):
        return 2
    
    def __init__(self):
        self.heatingTimeMin = 15
        self.currentTime = datetime.datetime.now()
        self.isOn = False    

    def status(self):
        if (self.isOn):
            return "Auton lämmitys päällä"
        else:
            return "Laitetaanko auton lämmitys päälle?"

    def turnOnOff(self, onOff):
        if (self.isOn and onOff):
            return "Auton lämmitys on jo päällä" 
        elif(self.isOn): 
            self.isOn = False 
            return "Auton lämmitys sammutetaan"  
        elif (onOff):
            self.isOn = True 
            return "Mihin aikaan lämpimäksi?" 
        else:
            return "Auton lämmitys ei ollut päällä" 

    def setTimer(self, hours, minutes):
        timerTime = datetime.datetime.strptime(str(hours) + ":" + str(minutes), "%H:%M")
        diff = self.currentTime - timerTime
        realDiff = self.heatingTimeMin - int(diff.seconds / 60)
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

    def status(self):
        if (self.isOn):
            return "Ovivahti päällä"
        else:
            return "Ovivahti pois päältä. Laitetaanko se päälle?"

    def turnOnOff(self, onOff):
        if (self.isOn and onOff):
            return "Ovivahti on jo päällä" 
        elif (self.isOn): 
            self.isOn = False 
            return "Ovivahti sammutetaan" 
        elif (onOff):
            self.isOn = True 
            return "Ovivahti laitettiin päälle."
        else:
            return "Ovivahti ei ollut päällä"
    
    def alert(self, sender):
        def send():
            sender.send("Joku tuli asuntoon")
        t = threading.Timer(30, send)
        t.start()
    
    def __str__(self):
        return "ovivahti"

class AirConditioning:

    def howManyParameters(self):
        return 1
    
    def __init__(self):
        self.isOn = False
        self.currentTemperature = 25
    
    def status(self):
        statusText = "Asunnon lämpötila on nyt " + str(self.currentTemperature)
        if (self.isOn):
            statusText += " ja ilmastointi on päällä. " + ""
        else:
            statusText += " ja ilmastointi ei ole päällä. " + "Laitetaanko se päälle?"
        return statusText
    
    def turnOnOff(self, onOff):
        if (self.isOn and onOff):
            return "Ilmastointi on jo päällä" 
        elif (self.isOn): 
            self.isOn = False 
            return "Ilmastointi sammutetaan"
        elif (onOff):
            self.isOn = True
            return "Ilmastointi on nyt päällä" 
        else:
            return "Ilmastointi ei ollut päällä"
    
    def __str__(self):
        return "ilmastointi"

class Help:

    def howManyParameters(self):
        return 0
    
    def status(self):
        helpText = ""
        helpText += "Palaa alkuun komennolla *lopeta*. Seuravilla komennoilla pääset\n"
        helpText += "vaikuttamaan kotisi laitteisiin: \n"
        # helpText += "\n"
        helpText += "sauna\n"
        helpText += "uuni\n"
        helpText += "auto\n"
        helpText += "ilmastointi\n"
        helpText += "ovivahti\n"
        # helpText += "\n"
        # helpText += "Voit myös antaa komennot suoraan seuraavassa muodossa:\n"
        # helpText += "sauna 1930 80/sauna pois\n"
        # helpText += "uuni 1930 200/uuni pois\n"
        # helpText += "auto 1930/auto pois\n"
        # helpText += "ilmastointi päällä/pois\n"
        # helpText += "ovivahti päällä/pois\n"
        return helpText

    def __str__(self):
        return "apua"
