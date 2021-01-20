## Primer prueba de Web Scrapping

# pip freeze > requirements.txt
# Instalar requests, bs4(beautifulsoup),pip install lxml, pip install xlsxwriter

# Librerías

import requests
from bs4 import BeautifulSoup

# Definir la página de donde se desea extraer información

url = 'https://www.ebay.com/globaldeals'

html = requests.get(url)
content = html.content # bytes
soup = BeautifulSoup(content,'lxml')

# Búsqueda del producto (info sacada de inspeccionar)

titulo = soup.findAll("h3",{"class":"dne-itemtile-title elipse-3"})
print(titulo)

# Obtener títulos de la página oficial de python

url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')  # text
print("List of all the h1, h2, h3 :")
for heading in soup.find_all(["h1", "h2", "h3"]):
    print(heading.name + ' ' + heading.text.strip())