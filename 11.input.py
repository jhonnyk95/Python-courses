#nombre = input('cual es tu nombre: \r\n')
#print(f'Hola {nombre}')

#leer datos que son numeros
edad = input('Cual es tu edad: ')
#Convertir edad (String) a int
edad = int(edad)

if edad >= 18:
    print('Ya puedes votar')
else:
    print('Aun no puedes votar')

# Mezcla con operadores
numero = input('Agrega un numero y te fire si es par o no \r\n')
numero = int(numero)

if numero % 2 == 0:
    print(f'El numero {numero} es par')
else:
    print(f'El numero {numero} es impar')