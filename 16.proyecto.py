import os #Libreria para importar archivos

#variable en mayuscula que significa que es una constante:

#Carpeta de contactos
CARPETA = 'contactos/' 

#Agrega la extension al archivo a crear
EXTENSION = '.txt' 

#Clase contacto
class Contacto:
    #Metodo contructor
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():

    #llamado de la funcion, revisa si la carpeta existe o no.
    crear_directorio()

    #Muestra el menu de opciones
    mostrar_menu()

    #preguntar al usuario la accion que desea
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)

        #Ejecuta las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opcion no valida, Intente nuevamente')

def eliminar_contacto():
    nombre = input('Seleccione el Contacto que desea eliminar: \r\n')
    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('Contacto eliminado corretamente')
    except IOError:
        print('No existe ese contacto')
    
    #Reiniciar app
    app()


def buscar_contacto():
    nombre = input('Seleccione el Contacto que desea buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Informacion del Contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)
    
    #reiniciar la app
    app()
    

def mostrar_contactos():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                #imprime los contenidos
                print(linea.rstrip())
            #Imprime un separador entre contactos
            print('\r\n')

def editar_contacto():
    print('Escribe el nombre de contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')
    
    #Revisar si el archivo existe antes de editarlo
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            #Resto de informacion
            nombre_contacto = input('Agregar el Nuevo Nombre:\r\n')
            telefono_contacto = input('Agregar el Nuevo Telefono:\r\n')
            categoria_contacto = input('Categoria la Nueva Categoria:\r\n')

            #instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribir el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n' )
            archivo.write('Telefono: ' + contacto.telefono + '\r\n' )
            archivo.write('Categoria: ' + contacto.categoria + '\r\n' )

            # Cerramos archivo
            archivo.close()

            #Renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            #Mostrar que el contacto se configuro exitosamente
            print('\r\n Contacto editado correctamente \r\n')

    else:
        print('Ese contacto no existe')

        #Reiniciar aplicacion
        app()

def agregar_contacto():
    print('Escribe los datos para agregar el nuevo Contacto')
    #variable para recibir el nombre
    nombre_contacto = input('Nombre del Contacto: \r\n')

    #Revisa si el archivo es igual o ya existe
    existe = existe_contacto(nombre_anterior)

    if not existe:
        
        #Para crear un archivo .txt con el nombre del contacto dentro de la carpeta
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

            # Resto de la informacion
            telefono_contacto = input('Agregar el Telefono:\r\n')
            categoria_contacto = input('Categoria Contacto:\r\n')

            #Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n' )
            archivo.write('Telefono: ' + contacto.telefono + '\r\n' )
            archivo.write('Categoria: ' + contacto.categoria + '\r\n' )

            #Mensaje de exito
            print('Contacto creado correctamente \r\n')
    
    else:
        print('Ese contacto ya existe')
    
    #Reinicia la app
    app()

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

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()