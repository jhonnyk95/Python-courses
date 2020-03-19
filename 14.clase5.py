# Polimorfismo:
# Es la habilidad de tener diferentes comportamientos basado 
# en que subclase se esta utilizando, relacionado muy estrechamente
# con herencia.
class Restaurant:
    
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #Atributo
        self.categoria = categoria
        self.precio = precio #Default: public, PROTECTEC con una _ ,
        #PRIVATE con dos __.
    
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')
    
    #GETTERS Y SETTER - GEt Obtener, SET = Agregar.
    def get_precio(self):
        return self.precio
    
    def set_precio(self, precio):
        self.precio = precio

#Crear una clase hijo de Restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, alberca):
        super().__init__(nombre, categoria, precio)
        self.alberca = alberca
    
    # Reescribir un metodo (debe llamarse igual)
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}, Alberca: {self.alberca}')
    
    #Agregar un metodo que solo exista en hotel
    def get_alberca(self):
        return self.alberca


hotel = Hotel('Hotel POO', '5 Estrellas', 200, 'Si')
hotel.mostrar_informacion()
alberca = hotel.get_alberca()
print(alberca)