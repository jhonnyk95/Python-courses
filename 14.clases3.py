# en este se lograra ver encapsulamiento:
# Permite restringir u ocultar el acceso a los datos dentro de
# la misma clase del mundo exterio (usualmente se modifica via
# metodos en la misma clase)
class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #atributo
        self.categoria = categoria
        self.__precio = precio # Default: Public, PROTECTED es con _ (guion bajo), PRIVATE __ (doble guion bajo)


    def mostrar_informacion(self):
         print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: $ {self.__precio}')

#Instanciar la clase
restaurant = Restaurant('Pizzeria Mexico', 'Comida Italiana', 50)
restaurant.__precio = 80 #no sera posible modificarlo con private
restaurant.mostrar_informacion()

restaurant2 = Restaurant('Hambuerguesa Python', 'Comida Casual', 20)
restaurant2.__precio = 40
restaurant2.mostrar_informacion()
#teniendo encuenta que necesito aprender cada vez mas
