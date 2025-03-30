import random
import spacy
import nltk

# Cargar el modelo de spacy
nlp = spacy.load('es_core_news_sm')

# Base de respuestas y patrones
respuestas = {
    "saludos": ["Hola, ¿cómo te va?", "¿Qué onda?", "Hola, ¿qué tal?"],
    "despedida": ["Adiós, espero no verte pronto", "Nos vemos... o no.", "Chao, no me hagas extrañarte."],
    "ayuda": ["Soy tu asistente, ¿qué necesitas?", "¿En qué puedo ayudarte? Aunque no espero que sea algo interesante."],
    "default": ["No sé qué decirte, ¿sabes?", "¿Y eso qué?"],
    "status": ["Mi sistema está perfecto, pero gracias por preguntar... supongo."]
}

# Función de respuesta básica
def responder(texto):
    doc = nlp(texto.lower())
    
    if "hola" in texto or "buenos días" in texto:
        return random.choice(respuestas["saludos"])
    elif "adiós" in texto or "chao" in texto:
        return random.choice(respuestas["despedida"])
    elif "ayuda" in texto or "qué puedes hacer" in texto:
        return random.choice(respuestas["ayuda"])
    elif "estado" in texto or "cómo estás" in texto:
        return random.choice(respuestas["status"])
    else:
        return random.choice(respuestas["default"])

# Función para simular la interacción
def interactuar():
    print("S.A.R.A. está activa. Puedes decir 'adiós' para salir.")
    
    while True:
        usuario = input("Tú: ")
        if "adiós" in usuario.lower() or "chao" in usuario.lower():
            print("S.A.R.A.: " + random.choice(respuestas["despedida"]))
            break
        else:
            respuesta = responder(usuario)
            print("S.A.R.A.: " + respuesta)

# Iniciar la interacción
if __name__ == "__main__":
    interactuar()
