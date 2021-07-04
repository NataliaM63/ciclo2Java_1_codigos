  #*** CONDICIONALES ***

a = 7

# print(f'a = {a}')
# if a > 0:   #si a es mayor que o entonces 
#     print(f'{a} es mayor que 0')   #imprimir 
# else:
#     if a == 0:
#          print('a es igual a 0')
#     else:
#         print(f'{a} es menor que 0') 

if a == 0:    # if --> si 
    print('a es igual a 0')
elif a > 0:   # elif --> entonces enlazar varios enlaces 
    print(f'{a} es mayor que 0')
else:         # else --> sino 
    print(f'{a} es menor que 0')

#----------
a = input("ingrese valor:   ")
b = input("Ingre valor:   ")

if a > 0 and b > 0:
    print("a y b son mayores que 0")
else: 
    if a < 0: 
                
                
                print(f'-----fin-----')