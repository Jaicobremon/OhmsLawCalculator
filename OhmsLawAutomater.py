#Importing all modules
from collections import Counter
import math
from numpy import number

#Saying introduction
print(" Welcome to Ohms law calculator version 1.0 !")

#Finction to calculate
def calculator():
    #Asking for what numbers are already given to the user
    print("Please choose which set of numbers you currently have")

    #Giving options
    set_of_options = input("A: Voltage and Current, B: Resistance and Current, C: Resistance and Voltage: ")

    #If option is A
    if set_of_options == "A":

        #Clarifying which option was chosen
        print("You have chosen A: Voltage and Current")

        #Asking for voltage and current
        Voltage = input("What is the voltage(V) ?: ")
        Current = input("What is the current(A) ?: ")

        #Dividing current from voltage
        Resistance = float(Voltage)/float(Current)

        #Printing the resistance
        print("The resistance is ---> " + str(Resistance))
    
    #If option is B
    if set_of_options == "B":

        #Clarifying which option was chosen
        print("You have chosen B: Resistance and Current")

        #Asking for resistance and Current
        Resistance = input("What is the current resistance ?: ")
        Current = input("What is the current(A) ?:")

        #Multiplying resistance by current
        Voltage = float(Resistance) * float(Current)

        #Printing the voltage
        print("The voltage is ---> " + str(Voltage))

    #If option is C
    if set_of_options == "C":
        
        #Clarifying which option was chosen
        print("You have chosen C: Resistance and Voltage")

        #Asking for resistance and voltage
        Resistance = input("What is the current resistance ?:" )
        Voltage = input("What is the current voltage(V) ?: ")
        
        #Dividing resitance from voltage`
        Current = float(Voltage)/float(Resistance)

        #Printing the current
        print("The current is ---> " + str(Current)) 

    #If an option other than A, B, C is given
    else:
        print("I cannot understand. Remember to use capital letters")

#Starting the function
calculator()