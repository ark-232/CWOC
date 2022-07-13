from playsound import playsound
import os
import pyttsx3

engine = pyttsx3.init() # pyttsx3 object creation
cwd = os.getcwd()

#make a loop that keeps the program running until the user wants to quit
def quit():
    print("Goodbye!")
    exit()

def play():
    print("Playing...")
    playsound(cwd+'\Audio\Reville.wav')

def light():
    engine.say("Lightning within 5 nautical miles!")
    engine.runAndWait()

def speak(usr):
    print(usr)  #!FIXME
    engine.say(usr)
    engine.runAndWait()
