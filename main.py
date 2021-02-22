import api
#make loop
run = True

#make compatable with py2 and 3
try:
    _input = raw_input
except NameError:
    _input = input

#start loop
while run:
    #get input
    inp = _input(">>")

    #check to see if inp is the same as a string
    if inp == "hello" or inp == "hi":
        print("Hi, how are you today?")
        feeling = _input(">>")
        if feeling == "good" or feeling == "fine":
            print ("Thats good")
        if feeling == "bad" or feeling == "not so good" or feeling == "very bad":
            print("Thats not so good")
    else:
        #what can you do
        if inp == "what can you do":
            api.list()
        else:
            #stop
            if inp == "stop" or inp == "quit":
                print("Stop in progress")
                run = False
            else:
                if inp == "add":
                    number1 = _input("give first number: ")
                    number2 = _input("give second number: ")
                    try:
                        out = api.add(int(number1), int(number2))
                    except ValueError:
                        out = "invalid"
                    print(str(out))
                else:
                    if inp == "thanks" or inp == "thank you":
                        print("Your welcome")
                    else:
                        #version
                        if inp == "version":
                            api.ver()
                        else:
                            if inp == "how are you today":
                                print("good")
                            else:
                                if inp == "what are you":
                                    print("I am a program made to help people")
                                else:
                                    api.NU()
