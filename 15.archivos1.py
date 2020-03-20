def app():

    with open('archivo.txt') as archivo:
       for contenido in archivo:
           print(contenido.rstrip()) #Abre un archivo creado, no es necesario cerrarlo

app()