#*** funciones de math y funciones de una libreria y un paquete
# import math #** esta es una libreria 
# import math as m  #**"m" un alias
#from math import sqrt, cos
from math import *  #esto no es recomendada para importar todas las funciones 
#solo importar las que se van a utilizar en el momento de realizar un programa

from funciones import *

# # Calcular potencia 
# pot = pow(2, 10)
# # Calcular raiz
raiz = sqrt(81)
# # Calcular coseno
# coseno = cos(45)
# # Calcular tangente
# tang = tan(90)

# print('potencia: ' +str(pot))
# print(raiz)
# print(coseno)
# print(tang)

#print(sumar(n1 + n2))
# print(sumar(10, 15))
# print(secante(90))
#help(sumar)

#** otra manera

var1 = 2
var2 = 10

pot = pow(var1, var2)

# print('potencia: ' +str(pot))
# print(str(var1) + 'elevado a la ' + var2 + 'es: ' + str(pot))
print('{} elevado a {} es: {}'.format(var1, var2, pot))












