import math
"App to help with Fahrenheit to Celsius conversion"

def actual_temp():

    celsius = input("Temperature in Celsius: ")

    temperature = 9 % 5 * float(celsius) + 32

    print("What is the temperature in Celsius?: " + str(celsius) + "°C")
    print(str(celsius) + "°C equals " + str("{:0.1f}".format(temperature)) + "°F")

actual_temp()