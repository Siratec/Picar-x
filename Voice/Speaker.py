import pyttsx3  

class Speaker:
    def __init__(self, rate=150, volume=1.0):
        self.engine = pyttsx3.init()  
        self.engine.setProperty('rate', rate) 
        self.engine.setProperty('volume', volume)  

    def hablar(self, texto:str):
        self.engine.say(texto)
        self.engine.runAndWait()  
