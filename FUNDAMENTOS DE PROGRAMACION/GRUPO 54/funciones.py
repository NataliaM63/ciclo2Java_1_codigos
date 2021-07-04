#"este docuemtno esta con operaciones"
from math import cos

def sumar(n1, n2) -> float:
    ''' Esta funcion permite sumar dos numeros
    recibidos como argumentos y
    retorna el total'''
    suma = n1 + n2
    return suma

def restar(n1, n2) -> float:
    ''' Esta funcion permite sumar dos numeros
    recibidos como argumentos y
    retorna el total'''
    resta = n1 - n2 
    return resta

def secante(n) -> float:
    sec = 1 / cos(n)
    return sec


# print('hola')
# print(sumar(1, 2))
# print(restar(n2=1, n1=2))   #print(restar(1, 2))



