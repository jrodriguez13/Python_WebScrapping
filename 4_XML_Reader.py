# Lectura, parseo y muestreo por consola del contenido de un XML

import urllib.request
import xml.etree.ElementTree as xml

url = 'https://www.w3schools.com/xml/simple.xml'

info = urllib.request.urlopen(url).read()
archivo = xml.fromstring(info.decode())

query = archivo.findall("food")
print("Cantidad de registros", len(query))
print('*' * 20)

for line in query:
    print('Nombre:', line.find('name').text)
    print('Precio:', line.find('price').text)
    print('Descripción:', line.find('description').text)
    print('Calorías:', line.find('calories').text)
    print('-' * 10)