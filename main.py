import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
import pywhatkit as kit
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)



def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def greet():
   hour = int(datetime.datetime.now().hour)
   if hour>=0 and hour<=12:
       speak("good morning boss,  i am ultron. i am a virtual artificial intelligence. how may i help you? ...")

   elif hour>=12 and hour<=18:
       speak("good afternoon boss,  i am ultron. i am a vitual artificial intelligence. how may i help you?..")

   else:
       speak("good evening boss, i am ultron. i am a virtual artificial intelligence. how may i help you?    ..") 
      # speak(" i am ultron. i am a virtual artificial intelligence. how may i help you?")  

def takeCommand():
   r = sr.Recognizer() 
   with sr.Microphone() as source:
      print("Listening...")
      r.pause_threshold = 0.5
      r.adjust_for_ambient_noise(source, duration=0.2)
      audio = r.listen(source)

   try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

   except Exception as e:
        print("Say that again please")
        return "None"
   return query

          
if __name__ == "__main__":
  greet()

while(1):

  query = takeCommand().lower()

  if 'wikipedia' in query:
     speak("Searching wikipedia")
     query = query.replace("wikipedia","")
     results = wikipedia.summary(query,sentences=5)
     speak("According to wikipedia")
     print(results)
     speak(results)

  
     
  elif 'open youtube'in query:
     speak("opening youtube for you, boss")
     webbrowser.open("youtube.com")

  elif 'greet everyone' in query:
     speak("hello Everyone")  

  elif 'google'in query:
     speak("opening google for you boss")
     webbrowser.open("google.com")

  elif 'no thanks'in query:
     print("ok boss have a good day")
     speak("ok boss, have a good day")
     
     sys.exit()

  elif 'hello' in query:
     speak("hello boss,  how may i help you?")   
 

  elif 'how are you' in query:
     speak("very well, boss. working with you makes my day. ")   

  elif 'start' in query:
     speak("ok boss! your wish is my command")  


  elif 'hi siri' in query:
     speak(" i am not siri. you are confusing me with some one else.") 

  elif 'hi alexa' in query:
     speak(" i am not alexa. you are confusing me with some one else.")    
  

  elif 'open code' in query:
     codepath = "C:\\Users\\mohdi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
     os.startfile(codepath)

  elif 'Search on google' in query:
     speak("boss, what should i search on google?")
     webbrowser.open("google.com")
     cm = takeCommand().lower()
     webbrowser.open(f"{cm}")


  elif 'open geeksforgeeks' in query:
     webbrowser.open("www.geeksforgeeks.org") 

  elif 'send message' in query:
     kit.sendwhatmsg("+91XXXXXXXXXX","hello papa",14,37)  

  elif 'play songs on youtube' in query:
     kit.playonyt("dandelions") 
     #kit.playonyt("night changes")
    # kit.playonyt("snap")
     
  elif 'pick a random number' in query:
     num = random.randint(0,100)
     print(num)
     speak(num)  

  elif 'give some advice' in query:
     advice =  [
        "believe in youself.",
        "do whatever it takes",
        "live life happy",
        "make your parents proud",
        "don't compare yourself to others"
         ]
     selected_advice = random.choice(advice)
     print(selected_advice)
     speak(selected_advice)
      
       
  elif 'tell me a joke' in query: 
     j = [
        "what did the left eye say to the right eye? > between you and me something smells>>>",
        "\n\t"
        "why was six afraid of seven? >>>  because seven ate nine"
     ]
     selected_joke = random.choice(j)
     print(selected_joke)
     speak(selected_joke)
      

  speak("boss,do you have any other work")   
      


     



     


        
