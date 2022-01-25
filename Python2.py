# Diseniar un sistema de puntos para el juego El reino del dragon:
# La idea es la siguiente: mientras el jugador vaya ganando, ira acumulando puntos.
# Ejemplo: Si el jugador entra en la primera cueva y gana el tesoro, se le acreditan 100 puntos, entra en la segunda cueva y gana el tesoro, se le acreditan otros 100 puntos. Si el jugador pierde, saldra en pantalla el total de los puntos que realizo y la opcion de empezar de nuevo.

'''

import random
import time

def introduccion():
    print ("\nEstamos en una tierra llena de dragones delante nuestro,")
    print ("se ven dos cuevas. En una cueva, el dragon es amigable")
    print ("y compartira el tesoro contigo. El otro dragon")
    print ("es codicioso y hambriento, y te va a comer ni bien te vea.")
    print ("")

def CambiarCueva():
    cueva = ""
    while cueva != "1" and cueva != "2":
        cueva = input('Elije la cueva 1 o 2: ')         
    return cueva

def cheqcueva(CambiarCueva):
    print ("\nTe acercas a la Cueva...")
    time.sleep(2)
    print ("Esta oscuro y tenebroso...")
    time.sleep(2)
    print ("Un gran dragon salta delante tuyo, abre su boca y...")
    print ("")
    time.sleep(2)
    
    p = 0

    FriendlyCueva = random.randint (1, 2)
   
    if CambiarCueva == str(FriendlyCueva):
        print ("Te entrega el tesoro...")
        p += 100
    else:
        print ("El dragon te come de un bocado....")
    
    return p


EmpezarNuevo = ("si")

puntaje = 0

while EmpezarNuevo == ("s") or EmpezarNuevo == ("si"):
   
    introduccion()
   
    NumCaverna = CambiarCueva()
   
    if cheqcueva(NumCaverna) == 100:
        puntaje += 100
    else:
        print (f'\nEl jugador ha perdido. \r\nPuntaje obtendio: {puntaje}')
   
    EmpezarNuevo = input('\nQuieres jugar de nuevo? (si o no): ')

'''

# Escribe un programa que te permita jugar a una version simplificada del juego Master Mind. El juego consistira en adivinar una cadena de numeros distintos. Al principio, el programa debe pedir la longitud de la cadena (de 2 a 9 cifras). Despues el programa debe ir pidiendo que intentes adivinar la cadena de numeros. En cada intento, el programa informara de cuantos numeros han sido acertados (el programa considerara que se ha acertado un numero si coincide el valor y la posicion).

'''

import random


longitud = int(input('Elija la longitud de la cadena (de 2 a 9 cifras): '))

while longitud <= 1 or longitud >= 10:
    longitud = int(input('Elija la longitud de la cadena (de 2 a 9 cifras): '))

numero = []

for i in range(longitud):
    i = random.randint(1, 9)
    numero.append(i)

#print (numero)

aciertos = 0

while aciertos != longitud:
    aciertos = 0
    intento = int(input('Intenta adivinar la cadena de numeros: '))
    copia = intento
    copia_longitud = longitud

    while copia > 0:
        copia_longitud -= 1
        digito = copia % 10
        if digito == numero[copia_longitud]:
            aciertos += 1
        copia = copia // 10
    if aciertos == 0:
        print ('\nNo has adivinado ningun valor.')
    elif aciertos == longitud:
        print (f'\nCon {intento} has adivinado todos los valores. \r\nFelicidades.')
    else:
        print (f'\nCon {intento} has adivinado {aciertos} valores.')

'''

# Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres ultimas letras tiene que decir que riman. Si coinciden solo las dos ultimas tiene que decir que riman un poco y si no, que no riman. 

'''

def palabras_que_riman(palabra1, palabra2):
    rima = ''
    if palabra1[-3] + palabra1[-2] + palabra1[-1] == palabra2[-3] + palabra2[-2] + palabra2[-1]:
        rima = 'Las palabras riman'
    elif palabra1[-2] + palabra1[-1] == palabra2[-2] + palabra2[-1]:
        rima = 'Las palabras riman un poco'
    else:
        rima = 'Las palabras no riman'
    return rima

p = input('Ingrese la primera palabra: ')
p2 = input('Ingrese la segunda palabra: ')

print (f'\r\n{palabras_que_riman(p, p2)}')


'''

# Has un programa que pida al usuario una cantidad de dolares, una tasa de interes y un numero de anios. Muestra por pantalla en cuanto se habra convertido el capital inicial transcurridos esos anios si cada anio se aplica la tasa de interes introducida. Recordar que un capital C dolares a un interes del x por cien durante n anios se convierte en C * (1 + x/100)elevado a n (anios). Probar el programa sabiendo que una cantidad de 10000 dolares al 4.5% de interes anual se convierte en 24117.14 dolares al cabo de 20 anios.

