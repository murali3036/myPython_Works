#Write a program which prompts the user for a Fahrenheittemperature,
#convert the temperature to Celsius and print out the converted temperature

#celsius * 1.8 = fahrenheit - 32

fahrenheit = float(input("Enter fahrenheit temp "))
conversionData =  (fahrenheit - 32)/1.8
print("Celcsius: "+str(conversionData))
