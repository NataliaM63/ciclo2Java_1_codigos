# #(11 mayo)
# #Anotaciones --> especificar el valor de entrada que soporta el paramentro y cual es la salida de la funcion 

# def saludar(nombre: str) -> None:
#     print("Hola " + nombre)
    
# #estudiante = saludar("Alex")

# def sumar(num1: int, num2: int) -> int:
#     return num1 + num2

# #print(sumar(5, 2))

# # print(sumar("Hola ", "Mundo"))

#  #**** FUNCIONES + if ***
 
def positivo_negativo(num: int) ->  str:
     
     if num > 0:
        x = f'{num} es mayor que 0'  
     elif num == 0:
         x = f'{num} es cero' 
     else: 
        x = f'{num} es menor que 0'
     return x
# numero = positivo_negativo(0)

# print(numero)

"""
- 'El ultimo digito de NUMERO es DIGITO' --->CONDICIONES:
                - si el digito es mayor que 5: 'y es mayor que cinco'
                - si el digito es 0: 'y es cero'
                - si el digito es menor que 6: 'y es menor que 6 y no es 0.'
"""

def ultimo_digito(num: int):
    if num >= 0:
        numero = str(num) [-1]
    else:
        numero = '-' + str(num) [-1]
        
    if numero > '5':
        out = f'El ultimo digito de {num} es {numero} y es mayor que cinco'
    elif numero == '0':
        out = f'El ultimo digito de {num} es {numero} y es cero'
    else:
        out = f'El ultimo digito de {num} es {numero} y es menor que 6 y no es 0'
    
    return out

import random


numero = random.randint(-1000, 1000)
# numero = 746
print(ultimo_digito(numero))
               
        


#*** CONDICIONALES ***

# a = 7

# print(f'a = {a}')
# if a > 0:   #si a es mayor que o entonces 
#     print(f'{a} es mayor que 0')   #imprimir 
# else:
#     if a == 0:
#          print('a es igual a 0')
#     else:
#         print(f'{a} es menor que 0') 

# if a == 0:    # if --> si 
#     print('a es igual a 0')
# elif a > 0:   # elif --> entonces enlazar varios enlaces 
#     print(f'{a} es mayor que 0')
# else:         # else --> sino 
#     print(f'{a} es menor que 0')

# #----------
# a = input("ingrese valor:   ")
# b = input("Ingre valor:   ")

# if a > 0 and b > 0:
#     print("a y b son mayores que 0")
# else: 
#     if a < 0: 
#      print(f'-----fin-----')
     
     
#Para explicar Try y Except utilizaremos de ejemplo una función que convierte 
# la temperatura en grados Fahrenheit a una temperatura en grados Celsius: 

# temperatura_fahr = input('Ingrese la temperatura en grados Fahrenheit: ')
# fahr = float(temperatura_fahr)
# cel = (fahr - 32.0) * 5.0 / 9.0
# print(cel)

# temperatura_fahr = input('Ingrese la temperatura en grados Fahrenheit: ')
# fahr = float(temperatura_fahr)
# cel = (fahr - 32.0) * 5.0 / 9.0
# print(cel)

# temperatura_fahr = input('Ingrese la temperatura en grados Fahrenheit: ')
# fahr = float(temperatura_fahr)
# cel = (fahr - 32.0) * 5.0 / 9.0
# print(round(cel,2))  ### round ayuda a aproximar el numero decimal despues de la coma 
     

# temperatura_fahr = input('Enter fahrenheit temperature')
# try:
#   fahr = float(temperatura_fahr)
#   cel = 5.0 / (9.0 * (fahr - 32.0))
#   print(cel)
# except:
#   print('Please enter a number') ## Solo pide el numero 
      
     
### 3. Matematico perezoso 

def pereira_es_potencia(x: int, y: int)-> bool:
      r = False
      if y == 1 or y == 0 or y < 0:
            r = False
      elif x ** 1 == y:
            r = True
      elif x ** 2 == y:
            r = True 
      elif x ** 3 == y:
            r = True
      elif x ** 4 == y:
            r = True
      elif x ** 5 == y:
            r = True
      return r

print(pereira_es_potencia(2, 1200))

