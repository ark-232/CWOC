import functions
# import datetime
# import wave
from playsound import playsound
import pyttsx3
engine = pyttsx3.init() # object creation

#make a loop that keeps the program running until the user wants to quit
while True:
    user_input = input()
    if user_input == "exit":
        print("Goodbye!")

    elif user_input == "play":
        print("Playing...")
        playsound("Reville.wav")

    elif user_input == "lightning":
        engine.say("Lightning within 5 nautical miles!")
        engine.runAndWait()

    #if the user inputs stop or exit, the program will stop
    elif user_input == "stop":
        print("Stopping...")
        exit()

    #make a text to speach function that will take the user input and speak it
    elif user_input == "speak":
        print("What would you like to speak?")
        user_input = input()
        engine.say(user_input)
        engine.runAndWait()
