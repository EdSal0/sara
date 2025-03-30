import random
from datetime import datetime
import requests
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pyperclip
from PyPDF2 import PdfReader
import csv
import moviepy.editor as mp
import time
import webbrowser
import pyttsx3
from pytube import YouTube
import easyocr
import subprocess
from pathlib import Path
import speech_recognition as sr
import pyautogui
import ctypes
import pygetwindow as gw
import shutil
import psutil
import platform

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
#sociales
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
def chiste():
    shiste=[
        "Un libro de matemáticas camina por la librería con una expresión sombría. ¿El motivo? Sus páginas rebosan de problemas, tanto así que su semblante se torna oscuro, como el misterio detrás de una ecuación sin resolver.",
        "En el gimnasio, una abeja se une a una clase de baile, pero no es cualquier baile, es ¡zum-ba! Y así, con su energía y ritmo, muestra que el vuelo no es su única habilidad destacada.",
        "Dos jardineros comparten un momento de complicidad en el jardín, pero, ¿qué diálogo podrían sostener? Nada, realmente, ya que en el reino verde, las conversaciones son un eco silencioso entre el murmullo de las hojas y el susurro de las flores.",
        "Una vaca, al ver salir el sol, emite un suspiro de satisfacción. ¿La razón? Con cada rayo luminoso, su producción láctea se dispara, creando un flujo constante de leche de día, la delicia matutina de los campos.",
        "Un electricista, experto en conectar circuitos y enredos, sufre el colmo de las desventuras: trabajar en un lugar con corriente irregular. ¿El resultado? Una jornada llena de cortocircuitos y chispas de humor.",
        "Los pájaros, esos seres alados de plumaje iridiscente, eligen la brevedad y la agilidad del vuelo para sus comunicaciones. Por eso, prefieren el trino fugaz de Twitter al discurso extenso y complejo de Facebook.",
        "En un encuentro familiar entre iguanas, una de ellas reconoce a su hermana gemela con un gesto de complicidad y cariño: '¡Iguanita!', susurra, revelando así el lazo indeleble que las une.",
        "La diversión llega al gimnasio cuando una abeja decide probar algo nuevo: una clase de baile. Y no cualquier baile, sino ¡zum-ba! Así, con su vuelo ágil y sus movimientos rítmicos, demuestra que la gracia y el vigor no son exclusivos de los seres humanos.",
        "El primo vegetariano de Bruce Lee, el famoso maestro de las artes marciales, se presenta al mundo como Broco Lee. Con su filosofía de paz y sus habilidades en el manejo del tofu, es un verdadero maestro del bienestar y la sostenibilidad.",
        "Dos jardineros comparten un momento de tranquilidad en el jardín, pero su comunicación es puramente visual, ya que en el reino verde las palabras son superfluas. Así, entre el murmullo de las hojas y el canto de los pájaros, se entienden sin necesidad de hablar.",
        "Un perro decide ampliar sus horizontes yendo a la escuela, no para aprender nuevos trucos, sino para nutrir su mente y ser más culto. Porque, después de todo, la educación no tiene límites, ¡ni siquiera para un buen chiste!",
    ]
    return random.choice(shiste)
def convertir_texto_a_voz_y_texto(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()
    print(texto)
def recomendacion_song():

    base_url = 'https://api.deezer.com/'
    def obtener_canciones_similares(artistas):
        canciones_similares = []

        for artista in artistas:
            params = {
                'q': artista,
                'limit': 5
            }
            response = requests.get(base_url + 'search', params=params)
            
            if response.status_code == 200:
                resultados = response.json().get('data', [])
                
                if resultados:
                    cancion_aleatoria = random.choice(resultados)
                    canciones_similares.append(cancion_aleatoria)
                    texto = f" {cancion_aleatoria['title']} de {cancion_aleatoria['artist']['name']}"
                    convertir_texto_a_voz_y_texto(texto)
                else:
                    mensaje = f'No se encontraron resultados para {artista}.'
                    convertir_texto_a_voz_y_texto(mensaje)
            else:
                mensaje = f'Error al obtener datos de Deezer para {artista}: {response.status_code}'
                convertir_texto_a_voz_y_texto(mensaje)
        
        return canciones_similares
    
    artistas = ['panda', 'iron maiden', 'el kuelgue', 'jose madero', 'CD9', 'The Doors', 'the beatles', 'AC/DC']
    canciones_similares = obtener_canciones_similares(artistas)
    
    convertir_texto_a_voz_y_texto("Esas son mis recomendaciones por hoy. ¡Espero que las disfrute y encuentre algo que le inspire tanto como a mí!")

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

    if canciones_similares:
        convertir_texto_a_voz('Aquí le presento una selección especial de canciones que creo que podrían encantarte. Espero que disfrutes de cada melodía tanto como yo disfruto compartiéndolas contigo:')
        for cancion in canciones_similares:
            titulo = cancion.get('title')
            artista = cancion.get('artist', {}).get('name')
            album = cancion.get('album', {}).get('title')
            print(f'Canción: {titulo} - Artista: {artista} - Álbum: {album}')
    else:
        print('"No encontré canciones para usted en esta ocasión. Pero no te preocupes, siempre hay una amplia gama de música por descubrir. ')
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
#funciones

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
def abrir_bloc_notas():
    try:
        subprocess.Popen(['notepad.exe'])
        convertir_texto_a_voz("Bloc de notas abierto correctamente.")
    except OSError as e:
        convertir_texto_a_voz(f"Error al abrir el Bloc de notas: {e}")
def dictado_por_voz():
    global dictado_por_voz_activo
    dictado_por_voz_activo = True
    convertir_texto_a_voz("Dictado por voz activado.")

    texto_dictado = ""

    while dictado_por_voz_activo:
        texto = reconocimiento_de_voz()  # Obtener el texto reconocido por voz
        if texto:
            texto_dictado += texto + " "

    guardar_dictado_por_voz(texto_dictado)

def guardar_dictado_por_voz(texto):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, "voz.txt")
    with open(file_path, "w") as file:
        file.write(texto)
    convertir_texto_a_voz("Dictado guardado como voz.txt en el escritorio.")

def minimizar_ventana_activa():
    ventana_activa = gw.getActiveWindow()
    if ventana_activa:
        ventana_activa.minimize()
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
def papelera():

    # Definir las constantes necesarias
    SHERB_NOCONFIRMATION = 0x00000001
    SHERB_NOPROGRESSUI = 0x00000002
    SHERB_NOSOUND = 0x00000004

    # Llamar a la función SHEmptyRecycleBinW de la biblioteca shell32.dll
    def vaciar_papelera():
        result = ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, SHERB_NOCONFIRMATION | SHERB_NOPROGRESSUI | SHERB_NOSOUND)
        if result != 0:
            raise ctypes.WinError(result)
    try:
        vaciar_papelera()
        convertir_texto_a_voz("La papelera de reciclaje se ha vaciado correctamente.")
    except Exception as e:
        convertir_texto_a_voz(f"Error al vaciar la papelera de reciclaje: {e}")
def mostrar_espacio_disco(drive_letter='C'):
    try:
        total, used, free = shutil.disk_usage(drive_letter + ':\\')
        #print(f"Espacio total en {drive_letter}: {total // (2**30)} GB")
        #print(f"Espacio usado en {drive_letter}: {used // (2**30)} GB")
        convertir_texto_a_voz(f"quedan libres en el disco {drive_letter}: {free // (2**30)} Gigas, el disco es de {total // (2**30)} Gigas, eso da un uso de {used // (2**30)} Gigas")
    except Exception as e:
        print(f"Error al mostrar el espacio en disco: {e}")
def monitorear_sistema():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    return f"Uso de CPU: {cpu_usage}%, Uso de memoria: {memory_info.percent}%"

def obtener_info_sistema():
    system_info = platform.uname()
    return f"El sistema es: {system_info.system}, con el usuario de: {system_info.node}, la máquina cuenta con un procesador: {system_info.machine}"
    #print(f"Release: {uname.release}")
    #print(f"Máquina: {uname.machine}")



def main(ruta_subcarpeta_descarga):
    crear_estructura_sara()
    Path="C:\\Users\\Edu_Sal\\Documents\\SARA\\AUDIO\\Yuridia - Amigos No por Favor (Primera Fila). flac"
    os.startfile(Path)
    convertir_texto_a_voz("Bienvenido, señor. En breve, todos los sistemas estarán completamente operativos. Mientras tanto, siéntase libre de relajarse y disfrutar de la espera. Que tenga un día maravilloso. Estoy lista para asistirle en todo lo que necesite.")
    pyautogui.hotkey('alt', 'f4')


    while True:
        # Obtener la entrada del usuario por voz
        comando_usuario = reconocimiento_de_voz()
        pyautogui.FAILSAFE = False
        if comando_usuario:
            #sociales
            if "hola" in comando_usuario or "Hola" in comando_usuario:
                convertir_texto_a_voz(saludo())
            elif "Cuéntame un chiste" in comando_usuario:
                convertir_texto_a_voz(chiste())
            elif "recomiéndame música" in comando_usuario:
                recomendacion_song()
            elif "gracias" in comando_usuario or "perfecto" in comando_usuario:
                convertir_texto_a_voz(denada())
            elif "hora" in comando_usuario or "dime la hora" in comando_usuario or "que hora es" in comando_usuario:
                convertir_texto_a_voz(f"Son las {now.strftime('%H:%M:%S')}")
            elif "estás despierta" in comando_usuario:
                convertir_texto_a_voz("Para usted señor. Siempre")
            elif "arriba ya llegó papá despierta" in comando_usuario:
                convertir_texto_a_voz("bienvenido señor")
                pyautogui.hotkey('enter')
            elif 'adios' in comando_usuario or 'cerrar' in comando_usuario:
                despedida()
                break
            #funciones
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
                    procesar_imagen(ruta_carpeta_principal)
                else:
                    convertir_texto_a_voz("No seleccionaste ninguna imagen.")  
            elif "abre el bloc de notas" in comando_usuario:
                abrir_bloc_notas()
            elif "activa el dictado por voz" in comando_usuario.lower():
                dictado_por_voz()
            elif "minimizar ventana" in comando_usuario.lower():
                minimizar_ventana_activa()
            elif "copiar" in comando_usuario.lower():
                pyautogui.hotkey('ctrl', 'c')
            elif "pegar" in comando_usuario.lower():
                pyautogui.hotkey('ctrl', 'v')
            elif "cortar" in comando_usuario.lower():
                pyautogui.hotkey('ctrl', 'x')
            elif "pdf" in comando_usuario:
                return pdf_extractor()
            elif "cambiar pestaña"in comando_usuario.lower():
                pyautogui.hotkey('ctrl', 'tab')
            elif "finalizar ventana" in comando_usuario.lower():
                pyautogui.hotkey('alt', 'f4')
            elif "muéstrame todo" in comando_usuario.lower() or "expande" in comando_usuario.lower():
                pyautogui.hotkey('win', 'tab')
            elif "cambiar ventana"in comando_usuario.lower():
                pyautogui.hotkey('alt', 'tab')
            elif "abre el administrador de archivos" in comando_usuario.lower():
                pyautogui.hotkey('win', 'e')
            elif "el escritorio" in comando_usuario.lower():
                pyautogui.hotkey('win', 'd')
            elif "abre el administrador de tareas" in comando_usuario.lower():
                pyautogui.hotkey('ctrl', 'mayus', 'esc')
            elif "actualiza" in comando_usuario.lower():
                pyautogui.hotkey('f5')
            elif "captura" in comando_usuario.lower():
                pyautogui.hotkey('win','printscreen')
            elif "clima" in comando_usuario.lower():
                ciudad = "Tecámac, MX"   
                tu_api_key = "f4fc7da4feccf91418b8596d53f09228"  
                respuesta = obtener_clima(ciudad, tu_api_key)
                convertir_texto_a_voz(respuesta)
            elif "noticias" in comando_usuario.lower():
                convertir_texto_a_voz(buscar_noticias())
            elif "busca" in comando_usuario.lower():
                buscar_en_sitios_populares(comando_usuario)
            elif "vacía la papelera" in comando_usuario:
                papelera()
            elif "almacenamiento" in comando_usuario.lower():
                mostrar_espacio_disco()
            elif "Dame información del pc" in comando_usuario.lower() or "ilustrame" in comando_usuario.lower():
                convertir_texto_a_voz(f"¡Por supuesto!. {obtener_info_sistema()}")
                convertir_texto_a_voz(f"Permítame brindarle los detalles sobre el estado actual del pc: {monitorear_sistema()}")
            elif "Abre Word" in comando_usuario.lower():
                 os.system("start winword")
            elif "Abre Excel" in comando_usuario.lower():
                 os.system("start excel")
            elif "Abre Powerpoint" in comando_usuario.lower():
                 os.system("start powerpnt")
            elif "ahorita vengo" in comando_usuario.lower():
                ctypes.windll.user32.LockWorkStation()
            elif "abre el navegador" in comando_usuario.lower():
                pyautogui.hotkey('f7', 'f7')
            elif "no me esperes despierta" in comando_usuario.lower() or "apaga el sistema" in comando_usuario.lower() or "ahí la ves" in comando_usuario.lower():
                convertir_texto_a_voz("que tenga un exelente dia")
                os.system("shutdown /s /t 5")
            #//music
            elif "a trabajar" in comando_usuario.lower():
                url = "https://open.spotify.com/playlist/3XVmOEL28PP0EvqhCx2uzr"
                webbrowser.open(url)
            elif "reproduce" in comando_usuario.lower():
                pyautogui.hotkey('space')
            elif "pausa" in comando_usuario.lower():
                pyautogui.hotkey('fn', 'f2')
            elif "baja volumen" in comando_usuario.lower():
                pyautogui.hotkey('fn', 'f5')
            elif "pantalla completa" in comando_usuario.lower():
                pyautogui.hotkey('f')
            elif "salir de pantalla completa" in comando_usuario.lower():
                pyautogui.hotkey('f')
            elif "sube volumen" in comando_usuario.lower():
                pyautogui.hotkey('fn', 'f6')
            elif "siguiente pista" in comando_usuario.lower():
                pyautogui.hotkey('fn', 'f3')
            elif "pista anterior" in comando_usuario.lower():
                pyautogui.hotkey('fn', 'f1')
            elif "repite esa" in comando_usuario.lower():
                pyautogui.hotkey('fn', 'f1')

            # Llama dos veces la tecla fn + f1 si es necesario
            elif "pista anterior" in comando_usuario.lower():
                pyautogui.hotkey('fn', 'f1')
                pyautogui.hotkey('fn', 'f1')
            else:
                respuesta = respuesta_no_entendido()
                convertir_texto_a_voz(respuesta)

if __name__ == "__main__":
    ruta_subcarpeta_descarga = crear_estructura_sara()
    main(ruta_subcarpeta_descarga)