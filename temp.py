# Created by : Andre Hazim
# Created on : 30 Oct. 2017
# Created for : ICS3UR
# This program converts the temperature in degrees celcius to degrees fahrenheight

def temperature(temperature_celcius):
    temperature_fahrenheight = 1.8 * temperature_celcius + 32
    print("It is "+ str(temperature_fahrenheight) + " in Fahrenheit")
    
temperature_celcius = raw_input("Please enter the degrees in Celsius :")
temperature_celcius =   float(temperature_celcius)
temperature(temperature_celcius)
