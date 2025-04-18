from Voice.Recognizer import escuchar
from Nlp.Mode_Detector import detectar_modo
from Robot.Modes_Control import ejecutar_modo
import threading
from Voice.Speaker import Speaker

modo_actual = None
hilo_modo = None
detener_evento = threading.Event()  

def correr_modo(modo):
    global hilo_modo, detener_evento

    detener_evento.clear()

    def correr():
        ejecutar_modo(modo, detener_evento)

    hilo_modo = threading.Thread(target=correr)
    hilo_modo.start()


def parar_modo_actual():
    global hilo_modo, detener_evento
    if hilo_modo and hilo_modo.is_alive():
        detener_evento.set()
        hilo_modo.join()
        

def main():
    global modo_actual
    Speaker.hablar("Mi nombre es Picar y estoy listo para comenzar")

    while True:
        texto = escuchar()
        PALABRA_CLAVE = "picar"

        if texto is None:
                continue
        else:
            if PALABRA_CLAVE in texto.lower():
                modo = detectar_modo(texto)

                if modo:
                    if modo != modo_actual:
                        print(f"Cambiando a modo: {modo}")
                        parar_modo_actual()
                        correr_modo(modo)
                        modo_actual = modo
                    else:
                        print(f"Re-ejecutando el modo actual: {modo}")
                        ejecutar_modo(modo)
                else:
                    print("No se reconoció ningún modo.")
            else:
                print("No se incluyó la palabra clave.")


if __name__ == "__main__":
    main()
