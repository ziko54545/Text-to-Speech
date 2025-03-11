import  pyttsx3
engine= pyttsx3.init()
name=input("entre your name")
engine.say(f"hello{name}")
engine.runAndWait()