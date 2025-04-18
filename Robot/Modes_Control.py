from Voice.Speaker import Speaker
from Robot.Modules.Seguimiento_Linea import Seguimiento_Linea
import time


def ejecutar_modo(modo, detener_evento):
    speaker = Speaker()
    seguidor_linea = Seguimiento_Linea()

    if modo == "consulta":
        speaker.hablar("Ejecutando modo CONSULTA")
        while not detener_evento.is_set():
            print("Consultando datos...")
            time.sleep(1)

    elif modo == "busqueda":
        speaker.hablar("Ejecutando modo BÚSQUEDA DE PERSONAS")
        while not detener_evento.is_set():
            print("Buscando personas...")
            time.sleep(1)

    elif modo == "grabacion":
        speaker.hablar("Ejecutando modo GRABACIÓN DE VIDEO")
        while not detener_evento.is_set():
            print("Grabando video...")
            time.sleep(1)

    elif modo == "lucha":
        speaker.hablar("Ejecutando modo LUCHA DE TOROS")
        while not detener_evento.is_set():
            print("Modo lucha en acción...")
            time.sleep(1)

    elif modo == "control_app":
        speaker.hablar("Ejecutando modo CONTROL POR APP")
        while not detener_evento.is_set():
            print("Controlando desde la app...")
            time.sleep(1)
    elif modo == "seguimiento_linea":
        speaker.hablar("Ejecutando modo SEGUIMIENTO DE LINEA")
        while not detener_evento.is_set():
           seguidor_linea.ejecutar()
    else:
        speaker.hablar("No se ha comprendido el modo")
