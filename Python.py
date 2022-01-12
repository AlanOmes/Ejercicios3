# Definir una funcion max() que tome como argumento dos numeros y devuelva el mayor de ellos. (Es cierto que python tiene una funcion max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

'''

def numero_mas_grande(num1, num2):
    num = 0
    if num1 > num2:
        num += num1
    elif num1 == num2:
        num = True    
    else:
        num += num2
    return num

numero = numero_mas_grande(1000, 1001)

if numero == True:
    print ('Los numeros son iguales')
else:
    print (f'El numero mas alto es {numero}') 

'''

#  Definir una funcion max_de_tres(), que tome tres numeros como argumentos y devuelva el mayor de ellos.

'''

def num_mas_alto(num1, num2, num3):
    num = 0
    if num1 > num2 and num1 > num3:
        num += num1
    elif num2 > num1 and num2 > num3:
        num += num2
    elif num3 > num1 and num3 > num2:
        num += num3
    else:
        num = True
    return num

numero = num_mas_alto(50, 1000, 500)

if numero == True:
    print ('Los numeros son iguales')
else:
    print (f'El numero mas alto es {numero}')

'''

# Definir una funcion que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la funcion len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

'''

def longitud(palabra_o_lista):
    l = 0
    for i in palabra_o_lista:
        l += 1
    return l

lista = ['a', 'b', 'c', 'd', 'e']

lon = longitud(lista)

print (lon)

'''

# Escribir una funcion que tome un caracter y devuelva True si es una vocal, de lo contrario devuelve False.

'''

def vocal(letra):
    vocales = ['a', 'e', 'i', 'o', 'u']
    letra = letra.lower()
    if letra in vocales:
        return True
    return False

'''

# Escribir una funcion sum() y una funcion multip() que sumen y multipliquen respectivamente todos los numeros de una lista. Por ejemplo: sum([1,2,3,4]) deberia devolver 10 y multip([1,2,3,4]) deberia devolver 24.

'''

def suma(lista):
    num = 0
    for i in lista:
        num += i
    return num

def multip(lista):
    num = 1
    for i in lista:
        num *= i
    return num

lista = [1, 2, 3, 4]

print (suma(lista))
print (multip(lista))

'''

# Definir una funcion superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en comun o devuelva False de lo contrario. Escribir la funcion usando el bucle for anidado.

'''

def listas_en_comun(lista1, lista2):
    for i in lista2:
        if i in lista1:
            return True
    return False

l = ['1', '2', '3']
l2 = ['3', '4', '5']

if listas_en_comun(l, l2) == True:
    print ('hola')

'''

# Definir una funcion generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") deberia devolver "xxxxx".

'''

def generar_n_caracteres(numero, caracter):
    return numero * caracter

print (generar_n_caracteres(5, 'a'))

'''

# Definir un histograma procedimiento() que tome una lista de numeros enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) deberia imprimir lo siguiente:

# ****
# *********
# *******

'''

def procedimiento(lista):
    for i in lista:
        print (i * '*')

lista = [1, 2, 3]

print (procedimiento(lista))

'''

# La funcion max() del ejercicio 1 y la funcion max_de_tres() del ejercicio 2, solo van a funcionar para 2 o 3 numeros. Supongamos que tenemos mas de 3 numeros o no sabemos cuantos numeros son. Escribir una funcion max_in_list() que tome una lista de numeros y devuelva el mas grande.

'''

def max_en_lista(lista):
    maxx = -99999
    for i in lista:
        if i > maxx:
            maxx = i
    return maxx

lista = [1, 4, 6, 7, 23, 64, 3, 8]

print (max_en_lista(lista))

'''

# Escribir una funcion mas_larga() que tome una lista de palabras y devuelva la mas larga. 

'''

def mas_larga(lista_de_palabras):
    palabra = ''
    for i in lista_de_palabras:
        if len(i) > len(palabra):
            palabra = i
    return palabra

lista = ['hola', 'caca', 'pis', 'casamiento', 'coche']

print (mas_larga(lista))

'''

# Escribir una funcion filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres. 

'''

def filtrar_palabras(lista, n):
    palabras = ''
    for i in lista:
        if len(i) > n:
            palabras += f' {i}'
    return palabras

lista = ['hola', 'caca', 'pis', 'casamiento', 'coche']

print (filtrar_palabras(lista, 3))

'''

# Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayusculas tiene. 

'''

def contador_mayusculas(texto):
    mayusculas = 0
    for i in texto:
        if i == i.upper() and i != " ":
            mayusculas += 1
    return mayusculas

texto = input('Escriba una cadena de texto: ')

print (f'La cadena de texto tiene {contador_mayusculas(texto)} letras mayusculas.') 

'''

# Construir un pequeno programa que convierta numeros binarios en enteros. 

'''

def binario_a_entero(binario):
    convertido = int(binario, 2)
    return convertido

print (binario_a_entero('1101'))

'''

# Escribir un pequeno programa donde:
# - Se ingresa el anio en curso.
# - Se ingresa el nombre y el anio de nacimiento de tres personas.
# - Se calcula cuantos anios cumpliran durante el anio en curso.
# - Se imprime en pantalla.

'''

def calcular_edad(anio_actual, anio_nacimiento):
    return anio_actual - anio_nacimiento


anio = int (input('Ingrese el anio en curso: '))

n1 = input ('Ingrese el nombre del primer alumno: ')
nacimiento_n1 = int(input ('Ingrese el anio de nacimiento del primer alumno: '))
n2 = input ('Ingrese el nombre del segundo alumno: ')
nacimiento_n2 = int(input ('Ingrese el anio de nacimiento del segundo alumno: '))
n3 = input ('Ingrese el nombre del tercer alumno: ')
nacimiento_n3 = int(input ('Ingrese el anio de nacimiento del tercer alumno: '))


print (f'\n{n1} cumplira {calcular_edad(anio, nacimiento_n1)} anios este anio.')
print (f'\n{n2} cumplira {calcular_edad(anio, nacimiento_n2)} anios este anio.')
print (f'\n{n3} cumplira {calcular_edad(anio, nacimiento_n3)} anios este anio.')


'''

# 


