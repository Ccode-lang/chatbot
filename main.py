def NU():
    print("I do not understand")

def add(a, b):
    total = a + b
    return total


def ver():
    print("Python Chatbot (1.0).")
    print("Type 'what can you do' to see what this version can do.")
    print("")

def list():
    print("hi or hello(program will ask how you are, answer and it will give an answer)")
    print("what can you do (shows this)")
    print("stop or quit(stops program)")
    print("add(add to numbers)")
    print("thanks(says 'your welcome')")
    print("how are you today(answers)")
    print("what are you(says purpose)")












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
            list()
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
                        out = add(int(number1), int(number2))
                    except ValueError:
                        out = "invalid"
                    print(str(out))
                else:
                    if inp == "thanks" or inp == "thank you":
                        print("Your welcome")
                    else:
                        #version
                        if inp == "version":
                            ver()
                        else:
                            if inp == "how are you today":
                                print("good")
                            else:
                                if inp == "what are you":
                                    print("I am a program made to help people")
                                else:
                                    NU()
