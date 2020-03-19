class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #atributo
        self.categoria = categoria
        self.precio = precio

    def mostrar_informacion(self):
         print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: $ {self.precio}')

#Instanciar la clase
restaurant = Restaurant('Pizzeria Mexico', 'Comida Italiana', 50)
restaurant.mostrar_informacion()

restaurant2 = Restaurant('Hambuerguesa Python', 'Comida Casual', 20)
restaurant2.mostrar_informacion()
#En este se vio adstracion y constructores