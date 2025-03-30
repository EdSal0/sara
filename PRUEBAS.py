import csv
from datetime import datetime, timedelta
import pyttsx3
import re

# Inicialización de la voz
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    if "spanish" in voice.languages or "es" in voice.id:
        engine.setProperty('voice', voice.id)
        break

def voz(text):
    """Función para hablar el texto con voz."""
    print(text)
    engine.say(text)
    engine.runAndWait()

# Ruta del archivo CSV donde se guardan los recordatorios temporales
recordatorios_file_temp = "recordatorios_temp.csv"

def obtener_proximo_dia(weekday):
    """Función para obtener el próximo día de la semana."""
    today = datetime.now()
    days_ahead = weekday - today.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    next_day = today + timedelta(days=days_ahead)
    return next_day

# Función para agregar un recordatorio
def agregar_recordatorio():
    try:
        voz("¿Para qué es el recordatorio?")
        recordatorio = input("¿Para qué es el recordatorio? ")  # Esto lo puedes sustituir con un input de voz si lo deseas.

        voz("¿Cuándo quieres que sea el recordatorio? (Por ejemplo, próximo miércoles)")
        fecha_texto = input("¿Cuándo quieres que sea el recordatorio? (Por ejemplo, próximo miércoles) ")

        # Detectar si el texto contiene "próximo miércoles"
        if "próximo miércoles" in fecha_texto.lower():
            fecha = obtener_proximo_dia(2)  # 2 es el índice para miércoles en Python (lunes=0, martes=1, miércoles=2, etc.)
            fecha_formateada = fecha.strftime("%Y-%m-%d %H:%M")
            voz(f"El próximo miércoles será el {fecha_formateada}. Ahora, ¿a qué hora es el recordatorio?")
            
            hora = input("¿A qué hora es el recordatorio? (Formato 24 horas, ejemplo 14:30) ")
            fecha_hora = f"{fecha.strftime('%Y-%m-%d')} {hora}"

            # Guardar el recordatorio
            with open(recordatorios_file_temp, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([recordatorio, fecha_hora])

            voz(f"Recordatorio para el {fecha_hora} agregado: {recordatorio}")
        else:
            voz("No entendí la fecha, por favor repite el comando.")
    except Exception as e:
        voz(f"Hubo un error al agregar el recordatorio: {e}")

# Función para listar los recordatorios
def listar_recordatorios():
    try:
        with open(recordatorios_file_temp, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            recordatorios = list(reader)

        if recordatorios:
            for idx, recordatorio in enumerate(recordatorios, 1):
                voz(f"Recordatorio {idx}: {recordatorio[0]} para {recordatorio[1]}")
        else:
            voz("No tienes recordatorios programados.")
    except Exception as e:
        voz(f"Hubo un error al listar los recordatorios: {e}")

# Ejecutar el comando
def ejecutar_comando():
    texto = input("Comando: ")

    if texto is None:  
        voz("No entendí, por favor repite.")
        return  

    texto = texto.lower()

    if "agregar recordatorio" in texto:
        agregar_recordatorio()
    elif "listar recordatorios" in texto:
        listar_recordatorios()
    else:
        voz("Comando no reconocido.")
        print("❌")

# Llamar a la función para ejecutar el comando
ejecutar_comando()
