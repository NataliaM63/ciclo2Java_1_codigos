
#formas de escriber una variable (nombres de variables)

# costo = 5000
# c = 5000

# costoTotal = 5000
# costo_total = 5000 

# costoTotalCamiseta = 5000
# costo_total_camiseta = 5000

# costo_tot_cam = 5000

# En Python, las variables son un nombre simbólico que es una referencia o puntero a un objeto. Las variables se utilizan para denotar objetos con ese nombre.

# var1 = 1.20
# print(var1)

# En el ejemplo de arriba, la variable var1 se refiere a un objeto float (decimal) que tiene el valor de 1.20

# var1=int(var1)
# print(var1)

# La variable var1 fue forzada a tomar el valor de un entero

# Suponga que asignamos el valor entero 120 a una nueva variable var2.

# var1 = 120
# var2 = var1
# print(var2)

# La variable var2 se refiere al mismo objeto al que apunta a porque Python no crea otro objeto. Python administra la memoria de manera eficiente si asignamos la misma variable a dos valores diferentes.
# Asignemos nuevos valores. Ahora ambas variables se referirán a los diferentes objetos.

# var1 = 120
# var2 = 200

# print(var1)
# print(var2)

# Errores al declarar una variable
# var 1 = 120
# @var1 = 120
# 1var = 120
# var-1 = 120
# Asignación múltiple
# Python nos permite asignar un valor a múltiples variables en una sola declaración, lo que también se conoce como asignaciones múltiples.

# Podemos aplicar múltiples asignaciones de dos maneras, ya sea asignando un solo valor a múltiples variables o asignando múltiples valores a múltiples variables.

# Asignación de un solo valor a varias variables

# var1 = var2 = var3 = 200
# print(var1)
# print(var2)
# print(var3)

# Asignar varios valores a varias variables

     # var1, var2, var3 = 10 , 20 , 30
     # print(var1)
     # print(var2)
     # print(var3)

# Tipos de datos integrados
# Python tiene varios tipos de datos integrados , como números (enteros, flotantes, números complejos), cadenas, listas, tuplas y diccionarios.

# Hoy veremos entero y flotantes (decimales).

# Python soporta dos tipos de números - enteros y números de punto flotante (decimales).

# Los números enteros son: - 1, 2, 22, 476,-99999
# Los float o decimales son: - 1.0, 2.22, 22.098, 476.1,-99999.9
# Para definir un entero, usa la siguiente sintaxis:

# mientero = 1
# type( mientero)
# int
# print(mientero)

# Para definir un float (decimal), se usa la siguiente sintaxis:

# mifloat = 1.0
# type(mifloat)
# float
# print(mifloat)
# 1.0
# mifloat2 = float(1)
# print(mifloat2)
# 1.0




# # Algunos sencillos ejemplos son:

# 2 + 3   # Suma

#esta suma retornada un float

# numero1 = 10
# numero2 = 9.99
# numero3 = numero1 + numero2
# print(numero3)
# print(type(numero3))

# 19.990000000000002
# float
# #esta suma retorara un float

# numero1 = 10.0
# numero2 = 9.99
# numero3 = numero1 + numero2
# print(numero3)
# type(numero3)

# # 19.990000000000002
# # float
# # #esta suma retornada un entero

# numero1 = 10
# numero2 = 10
# numero3 = numero1 + numero2
# print(numero3)
# print(type(numero3))

# # 20
# # # int
# print(8 - 5)   # Resta
# print(2 * 6)   # Multiplicacion 12 / 3  # Division 
# print(12 // 3) #Division entera
# # 4.0
# print(7 % 3)   # Modulo (retorna el remanente de la división)
# print(7 ** 2) #potencia al cuadrado
# print(2 ** 3) #potencia al cubo

# x = 15 + 18
# sqrt = x**(0.5) # raiz cuadrada
# print(sqrt)




# Paréntesis (P)
# Los paréntesis tienen la mayor precedencia y pueden ser usados para forzar una expresión a evaluar en el orden que se desee. Como las expresiones entre paréntesis se evalúan primero

# por ejemplo 2 * (3-1) es 4

print(2*(3-1))
# 4
print((1+1)**(5-2)) # es 8

print((1+1)**(5-2))
# 8
# También puede usar paréntesis para hacer una expresión más fácil de leer, como en (minuto * 100) / 60, incluso si no cambia el resultado.

minuto = 10

print((minuto * 100 )/ 60)
# minuto*100/60
# Exponenciación (E)
# La exponenciación tiene la siguiente precedencia más alta

# Así que 2**1+1 es 3, no 4,

# 2**1+1
# y 3*1**3 es 3, no 27.

# 3*1**3
# Multiplicación (M), División (D), Suma (A), Resta (S)
# La multiplicación y la división tienen la misma precedencia, que es mayor que Suma y resta, que también tienen la misma precedencia.

# Así que 2*3-1 es 5, no 4

# 2*3-1
# y 6+4/2 es 8, no 5.

# 6+4/2
# Misma precendencia
# Los operadores con la misma precedencia se evalúan de izquierda a derecha.

# Así que la expresión 5-3-1 es 1, no 3, porque el 5-3 ocurre primero y luego el 1 es restado de 2.

# 5-3-1
# Ejercicios rápidos
# 1) ¿Que imprime el siguiente programa ?
# x = 43 
# x = x +1 
# print(x)
# 2) Calcule el promedio de las siguientes variables
# var1 = 10
# var2 = 4
# var3 = 5.5
# var4 = 67
 
# print("El promedio de esos numeros es "+str(promedio))

