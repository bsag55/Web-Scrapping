# Web Scrapping 3: Descargar imagenes

# Librerías


#from PIL import Image
import PIL.Image
import io
import requests
import xlsxwriter
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox as MessageBox

# Variables

url = "https://merki.pe/bebidas"
carpeta = r'C:\Users\b55al\OneDrive\Escritorio\Carpetas\Python\Web Scrapping 3'

headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
"Accept-Encoding":"gzip, deflate",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"DNT":"1"
}

html = requests.get(url,headers=headers)
content = html.content
soup = BeautifulSoup(content,"lxml")

# Extracción de Imagenes

i = 1

for post in soup.findAll('div',{"class":"product-item"}):      # Los parámetros de las funciones de Soup se obtienen de analizar el HTML de la página

    # Título del producto
    titulo = post.find("h2",{"class":"product-title"}).text

    # URL Imagen muestra

    url_img = post.find('img')['src']

    # Petición al server

    r = requests.get(url_img)

    # Guardar imagen en Bytes y en RAM

    file = io.BytesIO(r.content)

    # Abrir la imagen desde memoria

    imagen = PIL.Image.open(file)

    # Guardar la imagen

    imagen.save(carpeta+"\\"+str(titulo)+".jpg")
    print(i)
    i += 1

MessageBox.showinfo("Proceso Terminado")