import sys
from setuptools import Command
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime as dt
from datetime import date 
import wikipedia as wp
import pyjokes
import subprocess as sp
import webbrowser as wb 
import PyPDF2 

listener = sr.Recognizer()
engine = pyttsx3.init()


def greeting():
    hour = int(dt.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Moring!")
    elif hour>=12 and hour<18:
        talk("Good Evening")
    else:
        talk("Good Evening!")
    engine.say("i am Tanmai. how may i help you!")
    engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()
greeting()
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
    except:
        pass
    return command

def run_tanmai():
    command = take_command()
    print(command) 
    if "play" in command:
        song = command.replace("play","")
        talk("playing " + song )
        pywhatkit.playonyt(song)
    elif "chrome" in command:
        talk("opening chrome")
        program = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        sp.Popen([program])
    elif "firefox" in command:
        talk("opening firefox")
        program1 = "C:\Program Files\Mozilla Firefox\Firefox.exe"
        sp.Popen([program1])
    elif "brave" in command:
        talk("opening brave browser")
        program = "C:\Program Files\BraveSoftware\Brave-Browser\Application\Brave.exe"
        sp.Popen([program])
    elif "vs code" in command:
        talk("opening vs code")    
        program = r"C:\Users\ANSHU\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        sp.Popen([program])
    elif "voice assistant" in command:
        talk("opening vs code setting up portfolio files for coding")
        program = "D:\Tanmai Voice Assistant\Tanmai.py"
        sp.Popen([program])
    elif "portfolio" in command:
        talk("opening your portfolio website")
        wb.open("https://anilrportfolio.web.app/")
    elif "calculator" in command:
        talk("opening calculator")
        wb.open("https://calculatekaro.web.app/")
    elif "guthub" in command:
        talk("opening your github account")
        wb.open("https://github.com/")
    elif "gmail" in command:
        talk("opening your gmail")
        wb.open("https://gmail.com/")
    elif "youtube" in command:
        talk("opening youtube")
        wb.open("https://youtube.com/")    
    elif "time" in command:
        time = dt.datetime.now().strftime("%I:%M %p")
        talk("current time is " + time)
        print(time)
    elif "date" in command:
        today = date.today()
        d2 = today.strftime("%B %d, %Y") 
        print(d2)
        talk("today is " + d2)
    elif "read" in command:
        pdf = open("oopsPython.pdf","rb")
        pdfreader = PyPDF2.PdfFileReader(pdf)
        pages = pdfreader.numPages
        for num in range(6,pages):
            page = pdfreader.getPage(num)
            text = page.extractText(page)
            talk(text)
    elif "wikipedia" in command:
        person = command.replace("wikipedia","")
        info = wp.summary(person,2)
        print(info)
        talk(info)    
    elif "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif "help" in command:
        print("1.opening of firefox,chrome & brave")
        print("2.seraching anything from wikipedia")
        print("3.say song I will play for you")
        print("4.opens gmail,github,portfolio,calculator")
        print("5.open the vs code")
    elif "stop" in command:
        talk("okay shutting down")
        sys.exit()
    elif "thank you" in command:
        talk("I'm honoured to serve")
        sys.exit()
    else:
        talk("command not found .try something different ")
        run_tanmai() 
    if command !="":
        run_tanmai()
    
run_tanmai()
