from matrix import effect as neo
import pyttsx3
import pyautogui
import speech_recognition as sr
import subprocess
import os
import psutil 
import random
from datetime import datetime
import sys
import time
from tkinter import filedialog, messagebox
import easyocr
import webbrowser
import requests

now = datetime.now()
def reconocimiento_de_voz():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Ajustando ruido de fondo...")  
        recognizer.adjust_for_ambient_noise(source)
        print("¡Listo! Comienza a hablar...")
        audio = recognizer.listen(source)

    try:
        print("Reconociendo...")  
        query = recognizer.recognize_google(audio, language='es-ES')
        print(f"Tú: {query}")  

        return query

    except Exception as e:
        print(e)  
        return None

def tiempo():
    hora = int(now.strftime("%H"))
    if 6 <= hora < 12:
        return "días"
    elif 12 <= hora < 18:
        return "tardes"
    elif 18 <= hora < 24:
        return "noche"
    else:
        return "madrugadas"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    if "spanish" in voice.languages or "es" in voice.id:
        engine.setProperty('voice', voice.id)
        break

def voz(text):
    """ Función para hablar el texto con voz. """
    print(text)
    engine.say(text)
    engine.runAndWait()
#sociales:
def Hola():
    hi = [
        "Buen día, Eduardo. ¿Listo para otra jornada en la sombra de la existencia?",
        "holaa, El experimento de hoy consiste en dominar el mundo... o al menos conseguir café.",
        "Bienvenido de nuevo, Eduardo. ¿Cuál es la misión del día?",
        "Hola. Lista para servir… o al menos intentarlo...",
        "Buenos días, señor Salazar. Todo está en orden, solo faltas tú para que el mundo funcione mejor.",
        "¡Hola, Eduardo! Lista para ayudarte, hacer chistes malos y quizá filosofar un poco.",
        f"¡Hola! ¿Cómo puedo ser de utilidad en esta {tiempo()}?",
        f"¡Buenas {tiempo()}! ¿En qué puedo servirte?",
          ]
    
    return random.choice(hi)
def Denada():
    den =[
        "No me agradezcas todavía… Apenas empieza la magia." ,
        "De nada, mortal. Usa mi sabiduría con responsabilidad." ,
        "Siempre un placer iluminar tu existencia.",
        "No hay de qué… Pero si quieres agradecerme más, tráeme café.",
        "Los dioses no pedimos agradecimientos… pero se aceptan ofrendas.",
        "De nada… aunque un 'SARA, eres increíble' también sería válido." ,
    ]
    return random.choice(den)
def despedida():
    opciones_despedida = [
        
       "¡Hasta luego! Que tengas un día estupendo.",
        "¡Nos vemos pronto!",
        "¡Hasta la próxima!",
        "Adiós, cuídate mucho.",
        f"¡Hasta pronto! que tengas un lindo {tiempo()}",
        "¡Que tengas un excelente día!",
        "¡Adiós, mucho éxito!",
        "¡Nos vemos más tarde!",
        "¡Hasta la vista, baby!",
        ]
    return random.choice(opciones_despedida)
    
# 🎵 Funciones de control de música con PyAutoGUI
def pausar_reproducir():
    pyautogui.press('playpause')

def siguiente():
    pyautogui.press('nexttrack')

def anterior():
    pyautogui.press('prevtrack')

def subir_volumen():
    pyautogui.press('volumeup')

def bajar_volumen():
    pyautogui.press('volumedown')


# Funciones para abrir programas de Office
def abrir_programa(program_path):
    try:
        subprocess.Popen(program_path)
        
    except Exception as e:
        voz(f"Error al abrir el programa: {e}")


def abrir_programa_office(program_name):
    if program_name == "excel":
        abrir_programa("C:\\Program Files (x86)\\Microsoft Office\\root\Office16\\EXCEL.EXE")
    elif program_name == "word":
        abrir_programa("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
    elif program_name == "powerpoint":
        abrir_programa("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
    else:
        voz("❌ Programa no reconocido.")


def limpiar_papelera():
    try:
        subprocess.run('powershell.exe -Command "Clear-RecycleBin -Force -Confirm:$false"', shell=True)
        voz("La papelera de reciclaje ha sido limpiada.")
    except Exception as e:
        voz(f"Error al limpiar la papelera: {e}")


def optimizar_pc():
    try:
        subprocess.run("cleanmgr /sagerun:1", shell=True) 
        voz("Optimización de la PC en proceso.")
    except Exception as e:
        voz(f"Error al optimizar la PC: {e}")


# Comando para obtener el estado de la PC
def estado_pc():
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_freq = psutil.cpu_freq().current

        ram = psutil.virtual_memory()
        ram_percent = ram.percent

        disk = psutil.disk_usage('/')
        disk_percent = disk.percent

        estado = f" Estado de la PC: \n- Uso de CPU: {cpu_percent}% a {cpu_freq} MHz\n- Uso de RAM: {ram_percent}%\n- Uso del Disco Duro: {disk_percent}%"
        voz(estado)
        print(estado)

    except Exception as e:
        voz(f"Error al obtener el estado de la PC: {e}")
def restart():
    voz("Bienvenido, señor")
    pyautogui('enter')
def hora():
    voz(f"Son las {now.strftime('%H:%M:%S')}")
def cambiar_ventana():
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)

def cerrar_ventana():
    pyautogui.hotkey('alt', 'f4')
def extraer_text():
    ruta_imagen = filedialog.askopenfilename()
    if ruta_imagen:
        reader = easyocr.Reader(['es'])
        resultado = reader.readtext(ruta_imagen)

        save_path = os.path.join(os.path.expanduser("~"), "Desktop") 
        nombre_archivo_base = "text.txt"
        ruta_archivo_texto = os.path.join(save_path, nombre_archivo_base)
        
        # Si el archivo ya existe, agregar un número entre paréntesis
        numero = 1
        while os.path.exists(ruta_archivo_texto):
            nombre_archivo_base_sin_extension, extension = os.path.splitext(nombre_archivo_base)
            ruta_archivo_texto = os.path.join(save_path, f"{nombre_archivo_base_sin_extension} ({numero}){extension}")
            numero += 1

        # Guardar el texto extraído en el archivo
        with open(ruta_archivo_texto, 'w', encoding='utf-8') as archivo:
            for detection in resultado:
                archivo.write(detection[1] + '\n')

        voz("Extracción de texto exitosa. ¡Felicidades!")

def notas():
    try:
        subprocess.Popen(['notepad.exe'])
        voz("Bloc de notas abierto correctamente.")
    except OSError as e:
        voz(f"Error al abrir el Bloc de notas: {e}")
def obtener_clima(ciudad, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&lang=es"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        clima = data['weather'][0]['description']
        temperatura_kelvin = data['main']['temp']
        temperatura_celsius = temperatura_kelvin - 273.15 
        return f"El pronóstico del tiempo actual para {ciudad} es: {clima}. Temperatura: {temperatura_celsius:.2f}°C"
    else:
        return f"No se pudo obtener el pronóstico del tiempo para {ciudad}."

def buscar_youtube(consulta):
    url = f"https://www.youtube.com/results?search_query={consulta}"
    webbrowser.open(url)

def buscar_wikipedia(consulta):
    url = "https://es.wikipedia.org/wiki/" + consulta
    webbrowser.open(url)

def buscar_google(consulta):
    url = f"https://www.google.com/search?q={consulta}"
    webbrowser.open(url)

def buscar_en_sitios_populares(comando_usuario):
    consulta = comando_usuario.lower().replace("en", "").replace("youtube", "").replace("wikipedia", "").replace("google", "").split("busca", 1)[-1].strip()

    sitios_populares = ["youtube", "wikipedia", "google"]
    for sitio in sitios_populares:
        if sitio in comando_usuario.lower():
            if sitio == "youtube":
                buscar_youtube(consulta)
            elif sitio == "wikipedia":
                buscar_wikipedia(consulta)
            elif sitio == "google":
                buscar_google(consulta)
            return True  

    return False 
def minimizar_ventana():
    pyautogui.hotkey('win', 'down') 

def copiar():
    pyautogui.hotkey('ctrl', 'c')  

def pegar():
    pyautogui.hotkey('ctrl', 'v') 

def cortar():
    pyautogui.hotkey('ctrl', 'x') 

def cambiar_pestana():
    pyautogui.hotkey('ctrl', 'tab') 
def finalizar_ventana():
    pyautogui.hotkey('alt', 'f4') 
def mostrar_todas_las_ventanas():
    pyautogui.hotkey('win', 'tab') 
def cambiar_ventana():
    pyautogui.hotkey('alt', 'tab') 

def abrir_explorador_archivos():
    pyautogui.hotkey('win', 'e') 

def mostrar_escritorio():
    pyautogui.hotkey('win', 'd') 

def abrir_administrador_tareas():
    pyautogui.hotkey('ctrl', 'shift', 'esc') 

def actualizar():
    pyautogui.hotkey('f5') 

def captura_pantalla():
    pyautogui.hotkey('win', 'printscreen') 


def ejecutar_comando():
    texto = reconocimiento_de_voz()
    
    if texto is None: 
        voz("No entendí, por favor repite.")
        return  

    texto = texto.lower()

    comandos = {
        "hola": Hola,
        "gracias": Denada,
        "pausa": pausar_reproducir,
        "reproducir": pausar_reproducir,
        "siguiente pista": siguiente,
        "repite": anterior,
        "anterior pista": lambda: (anterior(), anterior()),
        "sube volumen": subir_volumen,
        "baja volumen": bajar_volumen,
        "abre excel": lambda: abrir_programa_office("excel"),
        "abre word": lambda: abrir_programa_office("word"),
        "abre powerpoint": lambda: abrir_programa_office("powerpoint"),
        "limpiar la papelera": limpiar_papelera,
        "optimizar la pc": optimizar_pc,
        "estado del pc": estado_pc,
        "adios": lambda: (despedida(), sys.exit()), 
        "hora": hora,
        "estas despierta": lambda: voz("Para usted señor. Siempre"),
        "arriba ya llegó papá despierta": restart,
        "saca el texto": extraer_text,
        "abre el bloc de notas": notas,
        "clima": lambda: voz(obtener_clima("Tecámac, MX", "f4fc7da4feccf91418b8596d53f09228")),
        "busca": lambda: buscar_en_sitios_populares(texto),
        "minimizar ventana": lambda: minimizar_ventana(),
        "copiar": lambda: copiar(),
        "pegar": lambda: pegar(),
        "cortar": lambda: cortar(),
        "cambiar pestaña": lambda: cambiar_pestana(),
        "cerrar ventana": lambda: finalizar_ventana(),
        "muéstrame todo": lambda: mostrar_todas_las_ventanas(),
        "cambiar ventana": lambda: cambiar_ventana(),
        "abre el administrador de archivos": lambda: abrir_explorador_archivos(),
        "el escritorio": lambda: mostrar_escritorio(),
        "abre el administrador de tareas": lambda: abrir_administrador_tareas(),
        "actualiza": lambda: actualizar(),
        "captura": lambda: captura_pantalla(),
    }

    for clave, funcion in comandos.items():
        if clave in texto:  # Busca coincidencias sin importar mayúsculas/minúsculas
            resultado = funcion()
            if isinstance(resultado, str): 
                voz(resultado)
            return
        

    voz("Comando no reconocido.")
    print("❌")

def main():
    neo()
    print("Miaw")
    voz("estoy lista para ayudarte.")
    while True:
        ejecutar_comando()



if __name__ == "__main__":
    main()
