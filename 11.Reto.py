print("bienvenido al quiz :D")
puntaje = 0
pregunta1=input('Ella te ama?\r\n')
if pregunta1=='si' or 'SI':
    puntaje = puntaje+1
    print("FELICITACIONES ;3\r\n")
 
elif pregunta1== 'no' or 'NO':
    puntaje= puntaje-1
    print("Algun día Soldado ;D")
 
else:
    print('Oye tranquilo viejo si no te ama ;c')
#segunda pregunta
pregunta2=input('Te gustan los perros??\r\n')
if pregunta2=='si' or 'SI':
    puntaje =puntaje+1
    print('A mi tambien :D \r\n')
 
elif pregunta2== 'no' or 'NO': 
    puntaje = puntaje-1
    print("Que mal D:")
else:
    print('hmmm... malo')
 
#Ultima Pregunta
pregunta3=input('Te gusta el Rock :v? \r\n')
if pregunta3 == 'si' or 'SI':
    puntaje=puntaje+1
    print('Que buenos gustos tienes :D ')
elif pregunta3== 'no' or 'NO':
    puntaje=puntaje-1
    print("Que feos gustos xd \r\n")
else:
 
    print("que haces aqui viejo :v")
 
print(f'tu puntaje es igual a {puntaje}')