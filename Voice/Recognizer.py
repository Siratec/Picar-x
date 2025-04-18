import speech_recognition as sr

def escuchar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        try:
            audio = r.listen(source)
            texto = r.recognize_google(audio, language="es-ES")
            print("Has dicho:", texto)
            return texto.lower()
        except sr.UnknownValueError:
            print("Desconocido")
        except sr.RequestError:
            print("Error con el servicio de voz.")
        return None
