from playsound import playsound
import pyttsx3
engine = pyttsx3.init() # pyttsx3 object creation

#make a loop that keeps the program running until the user wants to quit
while True:
    user_input = input()
    if user_input == "exit" or user_input == "quit" or user_input == "stop":
        print("Goodbye!")
        exit()

    elif user_input == "play":
        print("Playing...")
        playsound("./Audio/Reville.wav")

    elif user_input == "lightning":
        engine.say("Lightning within 5 nautical miles!")
        engine.runAndWait()

    #make a text to speach function that will take the user input and speak it
    elif user_input == "speak":
        print("What would you like to speak?")
        user_input = input()
        engine.say(user_input)
        engine.runAndWait()
