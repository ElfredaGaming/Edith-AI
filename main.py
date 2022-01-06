import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import random
from random import choice
import asyncio
import wikipedia
from config import *
import pyjokes
import requests
import time
import json
import sys
import webbrowser
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
now = datetime.datetime.now()
clear = lambda: os.system('cls')

## Weather

URL = 'http://api.openweathermap.org/data/2.5/weather?q=Newmarket&appid=0c42f7f6b53b244c78a418f4f181282a&units=metric'
response = requests.get(URL)
data = response.json()
main = data['main']
tem = main['temp']
temp_feel_like = main['feels_like']
humidity = main['humidity']
pressure = main['pressure']
weather_report = data['weather']
wind_report = data['wind']

## Weather

def talk(text):
    engine.say(text)
    engine.runAndWait()


r = sr.Recognizer() 
def record_audio(ask=False):
    with sr.Microphone() as source: 
        if ask:
            talk(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio) 
        except sr.UnknownValueError:
            clear()
        except sr.RequestError:
            clear()
        return voice_data.lower()

while True:
    commands = record_audio()
    if 'song' in commands:
        song = commands.replace('play', '')
        talk('playing the requested song')
        pywhatkit.playonyt(song)
    elif 'time' in commands:
        time = datetime.datetime.now().strftime('%H:%M %p')
        talk('The current time is ' + time)
    elif 'exit' in commands:
        talk('Exiting Edith AI')
        clear()
        sys.exit()
    elif 'weather' in commands:
        talk(f'The Temperature In {location} is {tem}, and the feel like is {temp_feel_like}')
    elif 'temperature' in commands:
        talk(f'The Temperature In {location} is {tem}, and the feel like is {temp_feel_like}')
    else:
        clear()
