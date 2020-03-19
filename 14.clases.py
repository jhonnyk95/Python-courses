class Restaurant:

    def agregar_restaurant(self, nombre):
        self.nombre = nombre #atributo

    def mostrar_informacion(self):
         print(f'Nombre: {self.nombre}')

#Instanciar la clase
restaurant = Restaurant()
restaurant.agregar_restaurant('Pizzeria Mexico')
restaurant.mostrar_informacion()

restaurant2 = Restaurant()
restaurant2.agregar_restaurant('Hambuerguesa Python')
restaurant2.mostrar_informacion()

#Mostrar la informacion
print(f'Nombre Restaurant: {restaurant.nombre}\r\n')
print(f'Nombre Restaurant: {restaurant2.nombre}\r\n')