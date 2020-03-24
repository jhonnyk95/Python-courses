lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']

print(lenguajes)

#Los aarrays (lists) comienzan en la posicion 0
print (lenguajes[0]) #Python
print (lenguajes[1]) #Kotlin
print (lenguajes[2]) #Java
print (lenguajes[3]) #JavaScript

#Ordenar los elementos alfabeticamente
lenguajes.sort()
print(lenguajes)

#Acceder dentro de un elemento dentro del texto

aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

#modificando valores de un arreglo(list)
lenguajes[2] = 'php'
print(lenguajes)

#Agregar elementos a un arreglo (list)
lenguajes.append('Ruby')
print(lenguajes)

#Eliminar de un arreglo (list)
del lenguajes[1]
print(lenguajes)

#eliminar de un arreglo (list)
lenguajes.pop() #Eliminar el ultimo elemento
print(lenguajes)

#Eliminar con pop una posicion en especifico
lenguajes.pop(0)
print(lenguajes)

#Eliminar por nombre
lenguajes.remove('php')
print(lenguajes)