import urllib.request

# Lee una web y guarda el HTML en un archivo local

web = open('out\web.html', 'wb')
consulta = urllib.request.urlopen('https://lorem2.com')
consulta = consulta.read()
web.write(consulta)
web.close()