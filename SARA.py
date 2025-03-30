import random
from datetime import datetime
import requests
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pyperclip
from PyPDF2 import PdfReader
import csv
from geopy.geocoders import Nominatim
import moviepy.editor as mp
import time
import webbrowser
import pyttsx3
from pytube import YouTube
from moviepy.editor import VideoFileClip
import easyocr
from tkinter import filedialog
import subprocess
from pathlib import Path
import pyautogui
from selenium import webdriver
import pygetwindow as gw

now = datetime.now()
def crear_estructura_sara():
    ruta_documentos = Path.home() / "Documents"
    nombre_carpeta_principal = "SARA"
    ruta_carpeta_principal = ruta_documentos / nombre_carpeta_principal
    
    # Verificar si la carpeta principal ya existe
    if not ruta_carpeta_principal.exists():
        # Crear la carpeta principal si no existe
        os.makedirs(ruta_carpeta_principal)
        
    # Crear subcarpeta 'agenda' dentro de la carpeta 'SARA'
    ruta_subcarpeta_agenda = ruta_carpeta_principal / "agenda"
    if not ruta_subcarpeta_agenda.exists():
        os.makedirs(ruta_subcarpeta_agenda)
        
    # Crear el archivo CSV 'agenda.csv' dentro de la subcarpeta 'agenda'
    ruta_archivo_agenda = ruta_subcarpeta_agenda / "agenda.csv"
    if not ruta_archivo_agenda.exists():
        # Definir las columnas del archivo CSV
        columnas = ["Titulo", "Fecha_Hora"]
        
        # Crear el archivo CSV y escribir las columnas
        with open(ruta_archivo_agenda, "w", newline="", encoding="utf-8") as archivo_csv:
            escritor_csv = csv.DictWriter(archivo_csv, fieldnames=columnas)
            escritor_csv.writeheader()

    # Crear subcarpetas 'descargas' y 'Text' dentro de la carpeta 'SARA'
    subcarpetas = ["descargas", "Text"]
    for subcarpeta in subcarpetas:
        ruta_subcarpeta = ruta_carpeta_principal / subcarpeta
        if not ruta_subcarpeta.exists():
            os.makedirs(ruta_subcarpeta)

    # Crear subcarpetas específicas dentro de 'descargas'
    ruta_descargas = ruta_carpeta_principal / "descargas"
    subcarpetas_descargas = ["VIDEO", "AUDIO"]
    for subcarpeta_descarga in subcarpetas_descargas:
        ruta_subcarpeta_descarga = ruta_descargas / subcarpeta_descarga
        if not ruta_subcarpeta_descarga.exists():
            os.makedirs(ruta_subcarpeta_descarga)

    # Retornar la ruta de la carpeta principal 'SARA'
    return ruta_carpeta_principal

def convertir_texto_a_voz(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

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

def respuesta_no_entendido():
    notiendo = [
        "Wow, esto es un poco confuso para mí. ¿Podrías explicarlo de nuevo, pero de manera diferente?",
        "Lo siento, creo que me perdí en el camino. ¿Podrías simplificarlo un poco más?",
        "Hmm, necesito un poco más de claridad aquí. ¿Podrías ser más específico?",
        "¡Ups! Creo que necesito que me des más detalles para entender completamente.",
        "Lo siento, parece que hay un pequeño desajuste. ¿Podrías reformular tu pregunta?",
        "Parece que estoy en modo de pensamiento profundo aquí. ¿Podrías repetirlo de una manera más clara?",
        "¡Ahí va mi mente astronómica! ¿Podrías proporcionar un poco más de luz sobre esto?",
        "Parece que me he desviado un poco. ¿Podrías explicarlo de nuevo, pero de manera diferente?",
        "Hmm, me temo que necesito un poco más de contexto para entender completamente.",
        "Lo siento, parece que hay un pequeño desajuste aquí. ¿Podrías proporcionar más detalles?",
        "¡Ay! Creo que necesito que me des más información para conectar los puntos.",
        "Wow, esto es un poco complicado para mí. ¿Podrías simplificarlo un poco más?",
        "¡Vaya! Me temo que estoy navegando en aguas desconocidas aquí. ¿Podrías ser un poco más claro?",
    ]
    return random.choice(notiendo)
def saludo():
    opciones_saludo = [
        "Hola señor",
        "Hola, ¿en qué puedo ayudarte?",
        "¡Hola! Estoy aquí para asistirte.",
        f"¡Buenas {tiempo()}! ¿En qué puedo servirte?",
        "¡Hola, hola! ¿En qué puedo servirte hoy?",
        "¡Saludos! Aquí estoy, lista para ofrecer mi ayuda.",
        "hey you. Estoy aquí para asistirte en lo que necesites.",
        f"¡Hola! ¿Cómo puedo ser de utilidad en esta {tiempo()}?",
        f"{tiempo()}, porque buenas las canciones de morat"
    ]
    return random.choice(opciones_saludo)

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

def video(ruta_subcarpeta_descarga):
    url = input("URL: ")
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    def respuestas_descarga(video):
        respuestas = [
            f"Descargando el video llamado: {video.title} en una asombrosa resolución de {video.resolution}.",
            f"Preparando la descarga de video {video.title} con una calidad de {video.resolution}.",
            f"Descargando ahora mismo el video titulado: {video.title} en una calidad de {video.resolution}.",
            f"Iniciando descarga de {video.title} con una definición de {video.resolution}.",
            f"Iniciando la descarga de {video.title} con una asombrosa resolución de: {video.resolution}."
        ]
        return random.choice(respuestas)

    def mensaje_descarga():
        lito = [
            f"Descarga completada con éxito. ¡Listo para disfrutar de: {video.title}!",
            f"La descarga fue un éxito. Ahora puedes disfrutar de: {video.title} en alta calidad.",
            f"¡Descarga exitosa! Ahora tienes: {video.title} disponible para tu disfrute.",
            f"Descarga realizada con éxito. Disfruta de: {video.title} en la mejor calidad.",
            f"La descarga ha finalizado con éxito. Ahora puedes deleitarte con: {video.title} a una resolución de {video.resolution} ",
        ]
        return random.choice(lito)


    file_path = str(ruta_subcarpeta_descarga / "VIDEO")  
    video.download(output_path=file_path)

    respuesta = respuestas_descarga(video)
    convertir_texto_a_voz(respuesta)
    time.sleep(2)
    mensaje = mensaje_descarga()
    print(mensaje)
    convertir_texto_a_voz(mensaje)

def descargar_audio(ruta_subcarpeta_descarga):
    try:
        url = input("URL: ")
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()

        # Descargar el video
        convertir_texto_a_voz(f"¡Ahora mismo estoy descargando: {video.title} para que puedas disfrutarlo en un dos por tres!")
        file_path_video = os.path.join(ruta_subcarpeta_descarga, "AUDIO")  # Carpeta de video
        video_file_path = video.download(output_path=file_path_video)

        # Extraer audio
        clip = mp.VideoFileClip(video_file_path)
        audio_path = os.path.join(ruta_subcarpeta_descarga, "AUDIO", f"{video.title}.mp3")  # Ruta del archivo de audio
        clip.audio.write_audiofile(audio_path)
        clip.close()

        # Eliminar el archivo de video
        os.remove(video_file_path)

        convertir_texto_a_voz(f"¡Éxito total! Descarga finalizada y audio extraído de: {video.title}, ¡prepárate para disfrutarlo al máximo!")

    except Exception as e:
        convertir_texto_a_voz(f"Se produjo un error durante la descarga del audio")

def cambiar_ventana():
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)

def cerrar_ventana():
    pyautogui.hotkey('alt', 'f4')
def procesar_imagen(ruta_subcarpeta):
    ruta_imagen = filedialog.askopenfilename()
    if ruta_imagen:
        reader = easyocr.Reader(['es'])
        resultado = reader.readtext(ruta_imagen)

        save_path = ruta_subcarpeta/ "Text"
        nombre_archivo_base = 'texto_extraido.txt'
        numero = 1
        ruta_archivo_texto = os.path.join(save_path, nombre_archivo_base)
        while os.path.exists(ruta_archivo_texto):
            nombre_archivo_base_sin_extension, extension = os.path.splitext(nombre_archivo_base)
            ruta_archivo_texto = os.path.join(save_path, f"{nombre_archivo_base_sin_extension} ({numero}){extension}")
            numero += 1

        with open(ruta_archivo_texto, 'w', encoding='utf-8') as archivo:
            for detection in resultado:
                archivo.write(detection[1] + '\n')

        convertir_texto_a_voz("Extracción de texto exitosa. ¡Felicidades!")

def buscar_youtube(consulta):
    url = f"https://www.youtube.com/results?search_query={consulta}"
    webbrowser.open(url)

def buscar_wikipedia(consulta):
    url = "https://es.wikipedia.org/wiki/" + consulta
    webbrowser.open(url)

def buscar_google(consulta):
    url = f"https://www.google.com/search?q={consulta}"
    webbrowser.open(url)

def pdf_extractor():
    def extract_text():
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if not file_path:
            messagebox.showerror("Error", "No se ha seleccionado ningún archivo PDF.")
            return

        try:
            with open(file_path, 'rb') as file:
                reader = PdfReader(file)
                text = ''
                for page in reader.pages:
                    text += page.extract_text()

                text_box.delete(1.0, tk.END)  # Clear previous text
                text_box.insert(tk.END, text)
                messagebox.showinfo("Éxito", "Texto extraído correctamente del PDF.")

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo extraer el texto del PDF: {str(e)}")

    def copy_to_clipboard():
        text_to_copy = text_box.get(1.0, tk.END)
        pyperclip.copy(text_to_copy)
        messagebox.showinfo("Éxito", "Texto copiado al portapapeles.")

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Extractor de Texto de PDF")

    # Crear el botón para seleccionar el archivo PDF
    select_button = tk.Button(root, text="Seleccionar PDF", command=extract_text)
    select_button.pack(pady=10)

    # Crear un cuadro de texto para mostrar el texto extraído
    text_box = tk.Text(root, height=20, width=50)
    text_box.pack(padx=10, pady=5)

    # Crear el botón para copiar el texto al portapapeles
    copy_button = tk.Button(root, text="Copiar al Portapapeles", command=copy_to_clipboard)
    copy_button.pack(pady=10)

    root.mainloop()
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

def buscar_en_google(consulta):
    url = f"https://www.google.com/search?q={consulta.replace(' ', '+')}"
    webbrowser.open(url)

def abrir_bloc_notas():
    try:
        subprocess.Popen(['notepad.exe'])
        convertir_texto_a_voz("Bloc de notas abierto correctamente.")
    except OSError as e:
        convertir_texto_a_voz(f"Error al abrir el Bloc de notas: {e}")

def activar_dictado_por_voz():
    global dictado_por_voz_activo
    dictado_por_voz_activo = True
    convertir_texto_a_voz("Dictado por voz activado.")

def desactivar_dictado_por_voz():
    global dictado_por_voz_activo
    dictado_por_voz_activo = False
    convertir_texto_a_voz("Dictado por voz desactivado.")

def guardar_dictado_por_voz(texto):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, "texto_reconocido.txt")
    with open(file_path, "w") as file:
        file.write(texto)
    convertir_texto_a_voz("Texto guardado correctamente en el escritorio como texto_reconocido.txt.")

def obtener_clima(ciudad, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&lang=es"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        clima = data['weather'][0]['description']
        temperatura_kelvin = data['main']['temp']
        temperatura_celsius = temperatura_kelvin - 273.15  # Conversión de Kelvin a Celsius
        return f"El pronóstico del tiempo actual para {ciudad} es: {clima}. Temperatura: {temperatura_celsius:.2f}°C"
    else:
        return f"No se pudo obtener el pronóstico del tiempo para {ciudad}."

def denada():
    denanquius =[
        "¡Por supuesto!",
        "¡Con toda la onda!",
        "¡Sin rollo!",
        "¡Pa' eso estamos!",
        "¡Tranqui, aquí estoy!",
        "¡En la buena onda!",
        "¡Nada que agradecer, aquí para ti!",
        "¡A tu disposición, siempre!",
        "¡Con gusto!",
        #chileno
        "¡Dale, po!",
        "¡Al tiro, no hay drama!",
        "¡No te preocupes, aquí estoy!",
        "¡Cachai, siempre presente!",
        "¡La raja, aquí para ayudar!",
        "¡Ningún atado, para eso estoy!",
        "¡Buena onda, compadre!",
        "¡Por supuesto, poh!",
    ]
    return random.choice(denanquius)

def buscar_noticias(query=''):
    api_key = "a41172f4c1af464eb55ce8f10dfd8c44"
    country = 'mx'
    url = f"http://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}&q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get("totalResults", 0) > 0:
            articles = data["articles"][:3]
            news_headlines = [article['title'] for article in articles]
            news_list = "\n\n".join(news_headlines)
            convertir_texto_a_voz(f"Últimas noticias en México:\n\n{news_list}")
            print("Enlaces:")
            for article in articles:
                print(article['url'])
        else:
            return "No se encontraron noticias en México."
    else:
        convertir_texto_a_voz("Error al obtener noticias.")
def maximizar_ventana_activa():
    ventana_activa = gw.getActiveWindow()
    if ventana_activa:
        ventana_activa.maximize()
def minimizar_ventana_activa():
    ventana_activa = gw.getActiveWindow()
    if ventana_activa:
        ventana_activa.minimize()
def responder_pregunta(comando_usuario, ruta_subcarpeta_descarga):
    if "activa el dictado por voz" in comando_usuario.lower():
        activar_dictado_por_voz()
    elif "hola" in comando_usuario.lower():
        convertir_texto_a_voz(saludo())  # Corregir aquí
    elif "descarga" in comando_usuario.lower():
        convertir_texto_a_voz("¿Prefieres el encanto del video o la magia del audio para tu experiencia?")
        preferencia = input("Video o Audio: ").lower()
        if "video" in preferencia:
            video(ruta_subcarpeta_descarga)  
        elif "audio" in preferencia:
            descargar_audio(ruta_subcarpeta_descarga) 
    elif "saca el texto" in comando_usuario:
        convertir_texto_a_voz("¡Entendido! Por favor selecciona la imagen de la que deseas extraer el texto.")
        ruta_imagen = filedialog.askopenfilename()
        if ruta_imagen:
            ruta_carpeta_principal = crear_estructura_sara()  # Obtener la ruta de la carpeta principal de SARA
            procesar_imagen(ruta_carpeta_principal)  # Pasar la ruta de la carpeta principal como argumento
        else:
            convertir_texto_a_voz("No seleccionaste ninguna imagen.")
    elif "abre el bloc de notas" in comando_usuario:
        abrir_bloc_notas()
    elif "maximiza ventana" in comando_usuario.lower():
        maximizar_ventana_activa()
    elif "minimiza ventana" in comando_usuario.lower():
        minimizar_ventana_activa()
    elif "copiar" in comando_usuario.lower():
        pyautogui.hotkey('ctrl', 'c')
    elif "pegar" in comando_usuario.lower():
        pyautogui.hotkey('ctrl', 'v')
    elif "cortar" in comando_usuario.lower():
        pyautogui.hotkey('ctrl', 'x')
    elif "pdf" in comando_usuario:
        return pdf_extractor()
    elif "cambiar ventana" in comando_usuario:
        cambiar_ventana()
    elif "muestrame todo" in comando_usuario:
        pyautogui.hotkey('win', 'tab')
    elif "cerrar ventana" in comando_usuario:
        cerrar_ventana()
    elif "minimizar ventana" in comando_usuario:
        pyautogui.hotkey('alt', 'space', 'n')
    elif "nueva pestaña" in comando_usuario:
        pyautogui.hotkey('ctrl', 't')
    elif "cerrar pestaña" in comando_usuario:
        pyautogui.hotkey('ctrl', 'w')
    elif "cambiar pestaña"in comando_usuario.lower():
        pyautogui.hotkey('ctrl', 'tab')
    elif "abre el administrador de archivos" in comando_usuario:
        pyautogui.hotkey('win', 'e')
    elif "el escritorio" in comando_usuario:
        pyautogui.hotkey('win', 'd')
    elif "abre el administrador de tareas" in comando_usuario.lower():
        pyautogui.hotkey('ctrl', 'mayus', 'esc')
    elif "ahorita vengo" in comando_usuario:
        pyautogui.hotkey('win', 'l')
    elif "abre word" in comando_usuario:
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\OfficeXX\\WINWORD.EXE")
    elif "abre excel" in comando_usuario:
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\OfficeXX\\EXCEL.EXE")
    elif "abre power point" in comando_usuario:
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\OfficeXX\\POWERPNT.EXE")
    elif "actualiza" in comando_usuario:
        pyautogui.hotkey('f5')
    elif "captura" in comando_usuario:
        pyautogui.hotkey('win','printscreen')
    elif "clima" in comando_usuario:
        ciudad = "Ecatepec de Morelos, MX"  
        tu_api_key = "f4fc7da4feccf91418b8596d53f09228"  
        respuesta = obtener_clima(ciudad, tu_api_key)
        convertir_texto_a_voz(respuesta)
    elif "noticias" in comando_usuario:
        convertir_texto_a_voz(buscar_noticias())
    elif "gracias" in comando_usuario:
        convertir_texto_a_voz(denada())
    elif "busca" in comando_usuario.lower():
        buscar_en_sitios_populares(comando_usuario)
    elif "hora" in comando_usuario:
        return f"Son las {now.strftime('%H:%M:%S')}"
    elif "no me esperes despierta" in comando_usuario or "apaga el sistema" in comando_usuario or "ahí la ves" in comando_usuario:
        os.system("shutdown /s /t 5")
    elif "reinicia la pc" in comando_usuario:
        os.system("shutdown /r /t 1")
    elif "adios" in comando_usuario.lower() or "stop" in comando_usuario.lower():
        convertir_texto_a_voz(despedida()) 
        print("Deteniendo la grabación...")
    else:
        return respuesta_no_entendido()




def main():
    crear_estructura_sara()
    print("miaw")
    ciudad = "Tecámac, MX"  
    tu_api_key = "f4fc7da4feccf91418b8596d53f09228"  
    respuesta = obtener_clima(ciudad, tu_api_key)
    convertir_texto_a_voz(respuesta)

    ruta_subcarpeta_descarga = crear_estructura_sara()

    while True:
        usuario = input("User: ")
        if usuario.lower() == "adios":
            convertir_texto_a_voz("Adiós")
            break
        respuesta = responder_pregunta(usuario, ruta_subcarpeta_descarga)  # Pasar ruta_subcarpeta_descarga como argumento
        if respuesta is not None:
            convertir_texto_a_voz(respuesta)
            print("SARA:", respuesta)

if __name__ == "__main__":
    main()