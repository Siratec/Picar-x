import speech_recognition as sr
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

modos = {
    "consulta": [
        "quiero consultar", "modo consulta", "entra en modo consulta", "picar entra en modo consulta",
        "picar quiero consultar", "puedes consultar", "consulta ahora", "modo información",
        "modo análisis", "consultar datos", "revisa los datos", "accede a la información",
        "ver información", "consultar información", "picar, dame información"
    ],
    "busqueda": [
        "buscar personas", "modo búsqueda", "modo buscar personas", "picar busca personas",
        "busca a alguien", "necesito buscar personas", "puedes buscar personas", "modo localización",
        "encuentra personas", "ubica personas", "realiza búsqueda", "picar entra en modo búsqueda",
        "buscar datos de personas", "encuentra usuarios"
    ],
    "grabacion": [
        "grabar video", "quiero grabar", "picar graba", "picar empieza a grabar",
        "picar inicia grabación", "modo grabación", "graba esto", "modo video",
        "graba un video", "necesito grabar", "puedes grabar", "entra en modo grabación",
        "modo cámara", "picar entra en modo cámara", "grabar ahora"
    ],
    "lucha": [
        "modo lucha", "entra en modo lucha", "picar entra en modo lucha", "modo combate",
        "modo pelea", "inicia lucha", "lucha de toros", "modo agresivo", "modo batalla",
        "modo defensa", "activar modo lucha", "modo fuerza", "picar pelea", "picar ataca",
        "modo confrontación", "modo pelea"
    ],
    "control_app": [
        "modo control por app", "picar entra en modo app", "control desde la app", "modo remoto",
        "modo control remoto", "activa control por app", "modo teléfono", "control desde el celular",
        "control por celular", "aplicación de control", "picar, control por aplicación",
        "picar desde el móvil", "modo smartphone", "manejo desde la app", "app de control"
    ],
    "seguimiento_linea": [
        "modo seguimiento de línea", "picar sigue la línea", "activar línea", "modo seguir línea",
        "entra en seguimiento de línea", "seguir el camino", "seguir ruta", "modo línea",
        "seguir el trazo", "modo seguir pista", "modo seguir trayecto", "seguimiento de ruta",
        "picar sigue el recorrido", "modo rastreo de línea", "línea activa", "modo traza activa"
    ]
}


frases_referencia = []
mapeo_modo = []

for modo, frases in modos.items():
    for frase in frases:
        frases_referencia.append(frase)
        mapeo_modo.append(modo)

emb_modos = model.encode(frases_referencia, convert_to_tensor=True)

def detectar_modo(texto_usuario):
    texto_usuario = texto_usuario.lower()
    emb_usuario = model.encode(texto_usuario, convert_to_tensor=True)
    similitudes = util.pytorch_cos_sim(emb_usuario, emb_modos)[0]

    max_sim = similitudes.max().item()
    indice = similitudes.argmax().item()

    if max_sim > 0.5:
        return mapeo_modo[indice]
    else:
        return None

