# def suma(a,b):
#     return a + b 
# def resta(a,b):
#     return a / b
# def multiplicacion(a,b):
#     return a * b

#variable_calculadora = 100

#print(suma(5,2))

#*** funciones en calucladora con funciones*** 

import funciones_calc as calc

def calculadora(num1: int, num2: int, operacion: str) -> int:
    if operacion == '+':
        result = calc.suma(num1, num2)
    elif operacion == '-':
        result = calc.resta(num1, num2)
    elif operacion == '/':
        result = calc.divicion(num1, num2) 
    else:
        result = calc.multiplicacion(num1, num2)
        
    return result

def calculadora(num1: int, num2: int, operacion: str) -> int:
    if operacion == '+':
        result = calc.suma(num1, num2)
    elif operacion == '-':
        result = calc.resta(num1, num2)
    elif operacion == '/':
        result = calc.divicion(num1, num2) 
    else:
        result = calc.multiplicacion(num1, num2)
        
    return result

calculo = calculadora(5, 2, '*')

print(calculo)
# def suma(a: int, b: int) -> int:
#     return a + b 

# def resta(a: int, b: int) -> int:
#     return a / b

# def divicion(a: int, b: int) -> float:
    return a / b
    
    
# def multiplicacion(a: int, b: int) -> int:
#     return a * b