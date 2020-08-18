
# Python program to translate 
# speech to text and text to speech 

import os 
import platform


import speech_recognition as sr 
import pyttsx3  
  
r = sr.Recognizer()  
  
def SpeakText(command): 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 
activ=True
while(1):     
    
    try: 
        with sr.Microphone() as source2: 
            r.adjust_for_ambient_noise(source2, duration=2) 
            if not activ :
                print("Speak \"Jarvis\" to activate ... ")           

                audio2 = r.listen(source2) 
                print("...")
                platf=platform.system()

                text = r.recognize_google(audio2) 
                text = text.lower() 
                print("Did you say '"+text+"'")
                if text=="jarvis" :
                    print("Activated!")
                    activ=True
            if activ:
                text=""
                
                print("Speak anything ... ")           
                r.adjust_for_ambient_noise(source2, duration=2)
                audio2 = r.listen(source2) 
                print("...")
                platf=platform.system()

                text = r.recognize_google(audio2) 
                text = text.lower() 
                print("Did you say '"+text+"'")

                if(text=='good night'):
                     print('pc shutting down....')
                     playsound('caged_goodnight.mp3')
                     if(platf=="Linux"):
                        os.system("shutdown")
                        print("shutdown scheduled after 1 minute...")
                     else:
                        os.system("shutdown /s /t 2")
                     exit(); 

                elif(text[:10]=="search for"):
                    if(platf=="Linux"):
                        os.system("gio open https://www.google.com/search?q="+text[11:].replace(" ","+"))
                    else:
                        os.system("start https://www.google.com/search?q="+text[11:].replace(" ","+"))

                elif(text=="sleep"):
                    print("Good bye sir !")
                    activ=False

                elif text=="open mail":
                    if(platf=="Linux"):
                        os.system("gio open https://mail.google.com")
                    else:
                        os.system("start https://mail.google.com")    

                elif text=="open steam":
                    if(platf=="Linux"):
                        os.system("steam &")
                    else:
                        os.system("steam")    

                elif text=="take a screenshot":
                    if(platf=="Linux"):
                        os.system("gnome-screenshot")
                    else:
                        print("Not supported")    
              
    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
          
    except sr.UnknownValueError: 
        print("Coudln't Understand please try again !") 
