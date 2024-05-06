import os
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', 'mb-mary')
engine.setProperty('rate', 150)

text = "Hello, world!"
engine.say(text)
engine.runAndWait()
