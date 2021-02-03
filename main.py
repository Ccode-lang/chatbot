#!/bin/env python
from api import NU
#make loop
run = True

#start loop
while run:
    #get input
    inp = input(">>")
    
    #check to see if inp is the same as a string
    if inp == "hello":
        print("Hi, how are you today?")
        feeling = input(">>")
        if feeling == "good" or feeling == "fine":
            print ("Thats good")
        if feeling == "bad" or feeling == "not so good" or feeling == "very bad":
            print("Thats not so good")
    else:
        if inp == "what can you do":
            print("Answer your hellos(more functions to come)")
        else:
            if inp == "stop":
                print("Stop in progress")
                run = False
            else:
                NU()
