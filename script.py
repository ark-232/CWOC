import functions
import datetime
import wave
from playsound import playsound


user_input = input()
if user_input == "exit":
    print("Goodbye!")
    exit()
elif user_input == "play":
    print("Playing...")
    playsound("Reville.mp3")
    exit()
elif user_input == "warn":
    print("Warning!")
    playsound('warning.wav')
    exit()