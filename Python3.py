# Este programa pide primeramente la cantidad total de compras de una persona. Si la cantidad es inferior a $100.00, el programa dira que el cliente no aplica a la promocion. Pero si la persona ingresa una cantidad en compras igual o superior a $100.00, el programa genera de forma aleatoria un numero entero del cero al cinco. Cada numero correspondera a un color diferente de cinco colores de bolas que hay para determinar el descuento que el cliente recibira como premio. Si la bola aleatoria es color blanco, no hay descuento, pero si es uno de los otros cuatro colores, si se aplicara un descuento determinado segun la tabla que  aparecera, y ese descuento se aplicara sobre el total de compra que introdujo inicialmente el usuario, de manera que el programa mostrara un nuevo valor a pagar luego de haber aplicado el descuento.

# import random

# def tabla_color_descuento(dic):
#     print ('COLOR\t\t DESCUENTO\r\n')
#     for i in dic:
#         if dic[i] == 0:
#             dic[i] = 'NO TIENE'
#         else:
#             dic[i] = (f'{dic[i]} %')
#         print (f'{i}\t {dic[i]}')

# def colores_en_lista(dic):
#     colores = []
#     for i in dic:
#         colores.append(i)
#     return colores

# def color_random(lista):
#     return random.choice(lista)

# def calculo_descuento(precio, descuento):
#     return precio - descuento * precio / 100

# colores_descuento = {
#     'BOLA BLANCA' : 0,
#     'BOLA ROJA' : 10,
#     'BOLA AZUL' : 20,
#     'BOLA VERDE' : 25,
#     'BOLA AMARILLA' : 50,
# }

# salir = 2

# while salir != 1:
#     gasto = int (input('\r\nIntroduzca el precio total de la compra: '))
#     if gasto >= 100:
#         color = color_random(colores_en_lista(colores_descuento))
#         precioFinal = calculo_descuento(gasto, colores_descuento[color])
#         print('\r\nSU GASTO IGUALA O SUPERA LOS $100.00 Y POR LO TANTO PARTICIPA EN LA PROMOCION.\r\n')
#         print (tabla_color_descuento(colores_descuento))
#         print(f'\r\nALEATORIAMENTE USTED OBTUVO UNA {color}')
#         if color == 'BOLA BLANCA':
#             print('\r\nLO SENTIMOS, NO OBTUVO NINGUN DESCUENTO.')
#         else:
#             print (f'\r\nFELICIDADES! HA GANADO UN {colores_descuento[color]} DE DESCUENTO.')
#             print (f'\r\nSU NUEVO TOTAL A PAGAR ES: ${precioFinal}')
#     salir = int (input('\r\nSI DESEA SALIR PRESIONE 1 O DE LO CONTRARIO PRESIONE OTRO NUMERO: '))


