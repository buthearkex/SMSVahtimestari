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
        diffMin = diff.seconds/60
        #no time for heating
        if (diffMin < timeToHeat):
            totalMinutes = self.currentTime.minute + timeToHeat
            totalHours = self.currentTime.hour
            while totalMinutes > 60:
                totalHours += 1
                totalMinutes -= 60

            minuteStr = str(totalMinutes)
            #smoothly format minutes like 12.01 not 12.1
            if totalMinutes < 10:
                minuteStr = "0"+ str(self.targetTimeMin)

            warmAtStr = str(totalHours) + "." + minuteStr
            if temperature > 150:
                return "Polttouuni ei ehdi lämmetä ajoissa, mutta lämmitys aloitetaan. Valmis " + warmAtStr
            return "Sauna ei ehdi lämmetä ajoissa, mutta lämmitys aloitetaan. Valmis " + warmAtStr
        else:
            minuteStr = str(self.targetTimeMin)
            #smoothly format minutes like 12.01 not 12.1
            if int(self.targetTimeMin) < 10 and int(self.targetTimeMin) != 0:
                minuteStr = "0"+ str(self.targetTimeMin)
            warmAtStr = str(self.targetTimeHour) + "." + minuteStr
            if temperature > 150:
                return "Polttouuni lämpötilassa " + str(temperature) + " klo " + warmAtStr
            return "Sauna lämpötilassa " + str(temperature) + " klo " + warmAtStr

    def getCurrentTemperature(self):
        return self.currentTemperature

    def __str__(self):
        return "sauna"
    
class Oven:

    def howManyParameters(self):
        return 3
    
    def __init__(self):
        self.heatingSpeed = 9
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
            #when shutting down
            return "Uuni on päällä " + str(self.currentTemperature)+" °C. Sammuta komennolla *sammuta*."
        else:
            #when firing up
            return "Laitetaanko uuni päälle?"

    def turnOnOff(self, onOff):
        if (self.isOn and onOff):
            #firing up dialogue is going for second time by user
            return self.status() 
        elif (self.isOn): 
            #was on before
            self.isOn = False 
            return "Uuni sammutetaan."
        elif (onOff):
            #dialogue is going as normal
            self.isOn = True 
            return "Mihin aikaan uuni lämpimäksi?" 
        else:
            #when shutdown selected
            return "Uunia ei lämmitetä." 

    def setTimer(self, hours, minutes):
        self.targetTimeHour = hours
        self.targetTimeMin = minutes
        return "Mihin lämpötilaan?"

    def setTemperature(self, temperature):
        formattedTime = datetime.datetime.strptime(str(self.targetTimeHour) + ":" + str(self.targetTimeMin), "%H:%M")
        diff = formattedTime - self.currentTime
        timeToHeat = self.giveHeatingTimeMin(temperature)
        diffMin = diff.seconds/60
        #no time for heating
        if (diffMin < timeToHeat):
            totalMinutes = self.currentTime.minute + timeToHeat
            totalHours = self.currentTime.hour
            while totalMinutes > 60:
                totalHours += 1
                totalMinutes -= 60

            minuteStr = str(totalMinutes)
            #smoothly format minutes like 12.01 not 12.1
            if totalMinutes < 10:
                minuteStr = "0"+ str(self.targetTimeMin)

            warmAtStr = str(totalHours) + "." + minuteStr
            return "Uuni ei ehdi lämmetä ajoissa, mutta lämmitys aloitetaan. Valmis " + warmAtStr
        else:
            minuteStr = str(self.targetTimeMin)
            #smoothly format minutes like 12.01 not 12.1
            if int(self.targetTimeMin) < 10 and int(self.targetTimeMin) != 0:
                minuteStr = "0"+ str(self.targetTimeMin)
            warmAtStr = str(self.targetTimeHour) + "." + minuteStr
            return "Uuni lämpötilassa " + str(temperature) + " klo " + warmAtStr

    def getCurrentTemperature(self):
        return self.currentTemperature

    def __str__(self):
        return "uuni"

class Car:

    def howManyParameters(self):
        return 2
    
    def __init__(self):
        self.heatingTimeMin = 60
        self.currentTime = datetime.datetime.now()
        self.isOn = False    

    def status(self):
        if (self.isOn):
            #when shutting down
            return "Auton lämmitys on päällä. Sammuta komennolla *sammuta*."
        else:
            #when firing up
            return "Laitetaanko auton lämmitys päälle?"

    def turnOnOff(self, onOff):
        if (self.isOn and onOff):
            #firing up dialogue is going for second time by user
            return self.status() 
        elif (self.isOn): 
            #was on before
            self.isOn = False 
            return "Auton lämmitys katkaistu."
        elif (onOff):
            #dialogue is going as normal
            self.isOn = True 
            return "Mihin aikaan auto lämpimäksi?" 
        else:
            #when shutdown selected
            return "Autoa ei lämmitetä." 

    def setTimer(self, hours, minutes):
        formattedTime = datetime.datetime.strptime(str(hours) + ":" + str(minutes), "%H:%M")
        diff = formattedTime - self.currentTime
        timeToHeat = self.heatingTimeMin
        diffMin = diff.seconds/60
        #no time for heating
        if (diffMin < timeToHeat):
            totalMinutes = self.currentTime.minute + timeToHeat
            totalHours = self.currentTime.hour
            while totalMinutes > 60:
                totalHours += 1
                totalMinutes -= 60

            minuteStr = str(totalMinutes)
            #smoothly format minutes like 12.01 not 12.1
            if totalMinutes < 10:
                minuteStr = "0"+ str(minutes)

            warmAtStr = str(totalHours) + "." + minuteStr

            return "Liian vähän aikaa. Lämmitys aloitetaan nyt, valmista on " + warmAtStr
        else:
            mins = str(minutes)
            if len(mins) < 2:
                mins = "0" + mins
            warmAtStr = str(hours) + "." + mins
            return "Kelpaa, lämpenee valmiiksi kello " + warmAtStr
    
    def __str__(self):
        return "auto"

class DoorGuard:

    def howManyParameters(self):
        return 1
    
    def __init__(self):
        self.isOn = False

    def status(self):
        if (self.isOn):
            return "Ovivahti on päällä. Sammuta komennolla *sammuta*."
        else:
            return "Ovivahti pois päältä. Laitetaanko se päälle?"

    def turnOnOff(self, onOff):
        if (self.isOn and onOff):
            #firing up dialogue is going for second time by user
            return self.status()
        elif (self.isOn): 
            #was on before
            self.isOn = False 
            return "Ovivahti sammutetaan" 
        elif (onOff):
            #dialogue is going as normal
            self.isOn = True 
            return "Ovivahti laitettiin päälle."
        else:
            #when shutdown selected
            return "Ovivahtia ei laiteta päälle." 
    
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
            #firing up dialogue is going for second time by user
            return self.status()
        elif (self.isOn): 
            #was on before
            self.isOn = False 
            return "Ilmastointi sammutetaan"
        elif (onOff):
            #dialogue is going as normal
            self.isOn = True
            return "Ilmastointi on nyt päällä" 
        else:
            #when shutdown selected
            return "Ilmastointi ei ollut päällä"
    
    def __str__(self):
        return "ilmastointi"

class Help:

    def howManyParameters(self):
        return 0
    
    def status(self):
        helpText = """Palaa alkuun komennolla:
  *alkuun* tai *lopeta*

Seuraavilla komennoilla pääset vaikuttamaan kotisi laitteisiin: 
  *sauna* | *uuni* | *auto* | *ilmastointi* | *ovivahti*

Voit myös antaa komennot suoraan seuraavassa muodossa:
  *sauna päälle 1930 80* | *sauna pois*
  *auto 19.30*           | *auto pois*
  *ovivahti päälle*      | *ovivahti pois*"""
        return helpText

    def __str__(self):
        return "apua"
