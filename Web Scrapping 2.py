# Web Scrapping 2: Extraer producto y precio de Amazon

# Librerías

import requests
import xlsxwriter
from bs4 import BeautifulSoup

# Se crea el archivo excel a exportar

workbook = xlsxwriter.Workbook('Amazon.xlsx')
worksheet = workbook.add_worksheet('Productos_Amazon')
worksheet.write('A1','Producto')
worksheet.write('B1','Precio')

# Se definen para pasar el proceso de autenticación

headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
"Accept-Encoding":"gzip, deflate",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"DNT":"1"
}

url = "https://www.amazon.com/s?k=apple&language=es_US" # Se podría con format y un for iterar en las diferentes páginas

html = requests.get(url, headers = headers)
content = html.content
soup = BeautifulSoup(content,'lxml')
#print(soup)


# Recorrer los contenedores para extraer el título y el precio (potencial extracción de otros datos)

row = 1

for post in soup.findAll("div",{"class":"a-section a-spacing-medium"}):
    titulo = post.find("a",{"class":"a-link-normal a-text-normal"})
    precio = post.find("span",{"class":"a-offscreen"})
    if precio is not None:
        print(titulo.text)
        print(precio.text)
        worksheet.write(row,0,titulo.text)
        worksheet.write(row,1,precio.text)
        row += 1
workbook.close()