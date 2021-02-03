from api import NU
from api import add
#make loop
run = True

#start loop
while run:
    #get input
    inp = input(">>")

    #check to see if inp is the same as a string
    if inp == "hello" or inp == "hi":
        print("Hi, how are you today?")
        feeling = input(">>")
        if feeling == "good" or feeling == "fine":
            print ("Thats good")
        if feeling == "bad" or feeling == "not so good" or feeling == "very bad":
            print("Thats not so good")
    else:
        #what can you do
        if inp == "what can you do":
            print("Answer your hellos(more functions to come)")
        else:
            #stop
            if inp == "stop":
                print("Stop in progress")
                run = False
            else:
                if inp == "add":
                    number1 = input(">>")
                    number2 = input(">>")
                    out = add(int(number1), int(number2))
                    print(str(out))
                else:
                    NU()
