# Scrapping OFFLINE. En base al archivo HTML descargado, se parsean diferentes 
# labels del mismo y se muestran por pantalla

#Parsear el <title>
def title():
    web = open('out\web.html', 'rb')
    inicio = '<title>'
    fin = '</title>'
    for linea in web.readlines():
        linea = str(linea)
        if inicio in linea:
            x = linea.find(inicio)
            x = x + len(inicio)
            y = linea.find(fin)
            print(linea[x:y])
    web.close()
    
#Parsear los <li>
def list():
    web = open('out\web.html', 'rb')
    inicio = '<li>'
    fin = '</li>'
    for linea in web.readlines():
        linea = str(linea)
        if inicio in linea:
            if not '<a href' in linea:
                x = linea.find(inicio)
                x = x + len(inicio)
                y = linea.find(fin)
                print(linea[x:y])
    web.close()


if __name__ == '__main__':
    title()
    list()