# Revisar si una condicion es mayor a
balance = 0
if balance > 0:
    print('Puedes pagar')
else:
    print('no tienes saldo')

#like 
likes = 190
if likes >= 200:
    print('Excelente, 200 likes')
else:
    print('casi llegas a los 200')

# if con texxto
lenguaje = 'PHP'
if not lenguaje == 'Python':
    print('Exelente decision')

#Evaluar un boolean
usuario_autenticado=True

if usuario_autenticado:
    print('Acceso al sistema')
else:
    print('Debes iniciar session')

#evaluar un elemento de una lista
lenguajes =['python', 'Kotlin', 'Java', 'JAvaScript','PHP']

if 'PHP' in lenguajes:
    print:('PH Si existe')
else:
    print('No esta en la lista')

#If Anidados
usuario_autenticado = True
Usuario_admin = True

if usuario_autenticado:
    if Usuario_admin:
        print('Acceso total')
    else:
        print('Acceso al sistema')
else:
    print('Debes iniciar sessio')