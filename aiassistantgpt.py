import sys
from setuptools import Command
import speech_recognition as sr
import pyttsx3
import openai

API_KEY="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"
openai.api_key = API_KEY
messages =[]
messages.append({"role":"system","content":"Ai assistant"})



listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source,duration=0.3)
            print("listening...")
            talk("listening")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "tanmai" in command:
                command = command.replace("tanmai","")
            if "tanmay" in command:
                command = command.replace("tanmay","")
            return command
    except:
        pass
    

def run_tanmai():
    command = take_command()
    command = "what is python in 50 words"
    print(command) 
    messages.append({"role":"system","content":command})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role":"assistant","content":reply})
    print("\n"+reply+"\n")
    talk(reply)
    if command=="stop":
        talk("okay shutting down")
        sys.exit()
    if command=="thank you":
        talk("I'm honoured to serve")
        sys.exit()
     
run_tanmai()