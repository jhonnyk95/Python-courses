playlist = {} #Diccionario vacio
playlist['canciones'] = [] #lista vacia de canciones

#funcion principal
def app():
   #Agregar playlist
   agregar_playlist = True
   while agregar_playlist:
       nombre_playlist = input('como deseas nombrar la playlist? \r\n')
       if nombre_playlist:
           playlist['nombre'] = nombre_playlist
           # Ya tenemos un nombre
           agregar_playlist = False

           #llamando la funcon para agregar funciones
           agregar_canciones()

def agregar_canciones():
    #Bandera para agregar canciones
    agregar_cancion = True

    while agregar_cancion:
        #Preguntar al usaurio que cancion desea agregar
        nombre_playlist = playlist['nombre']
        pregunta= f'Agrega canciones para la playlist {nombre_playlist}: \r\n'
        pregunta += 'Escribe "x" para dejar de agregar canciones \r\n'

        cancion = input(pregunta)

        if cancion == 'x':
            #Dejar de agregar canciones
            agregar_cancion = False

            #Mostrar resumen de la playlist
            mostrar_resumen()
        else:
            #Agregar las canciones a la playlist
            playlist['canciones'].append(cancion)

            print(playlist)

def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist} \r\n')
    print('Canciones: \r\n')
    for cancion in playlist['canciones']:
        print(cancion)

app()