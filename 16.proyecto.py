import os #Libreria para importar archivos
#variable en mayuscula que significa que es una constante:
CARPETA = 'contactos/' #Carpeta de contactos

def app():

    crear_directorio()##llamado de la funcion, revisa si la carpeta existe o no.

    #Muestra el menu de opciones
    mostrar_menu()

    #preguntar al usuario la accion que desea
    preguntar = True
    while preguntar:
        opcion = input(f'Seleccione una opción: \r\n')
        opcion = int(opcion)

        #Ejecuta las opciones
        if opcion == 1:
            print('Agregar contacto')
            preguntar = False

def mostrar_menu():
    print('Selecione del menu lo que desea hacer:')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')

def crear_directorio():
    #if not os.path.exists('contactos/'): #Si la carpeta contacto no existe
    if not os.path.exists(CARPETA):
        #os.makedirs('contactos/') #Crea la carpeta!
        os.makedirs(CARPETA)
    else:
        print('La carpeta contactos ya existe')


app()