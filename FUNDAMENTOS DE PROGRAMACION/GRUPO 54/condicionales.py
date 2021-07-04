###*** DECISONES SIMPLES - SECUENCIA

#programa decisiones_en_secuencia
# Variables
     # entero:   num
#Inicio 
     # Escriba "digite un numero entero"
     # lea num
     
     # Si num <0
            # Esciba "el numero digitado es negativo"
     # Si num >0
            # Escriba "el numero digitado es positivo"
     # Si num = 0
            # Escriba "el numero digitado es cero"
            
###*** AHORA A CODIGOS ***###
# num = int(input())
# if num > 0:
#     print("El numero ", num, "es positivo")
# if num < 0:
#     print("El numero ", num, "es negativo")
# if num == 0:
#     print("El numero ", num, "es nulo")


###*** DECISIONES EN CASCADA

# // algoritmo desicion_en_cascada
# // variables 
#     entero: num
# inicio
#     escriba "por favor, digite un numero entero"
#     lea num 
#     si num < 0
#          num = num * (-1)
#     fin si
#     si num > = 1 y num < = 9
#          escriba "el numero tiene 1 digito"}
#     Sino 
#          si num > = 10 y num < =99
#              escriba "el numero tiene 2 digitos"
#          sino 
#              si num > = 100 y num < = 999
#                  escriba "el numero tiene 3 digitos"
#              sino
#                  si num > = 1000 y num < = 9999
#                      escriba "el numero tiene 4 digitos"
#                  sino 
#                      escriba "el numero tiene mas de 4 digitos"
#                  fin_si
#              fin_si
#          fin_si
#      fin_si
# fin 

# num = int(input("por favor, digite un numero entero"))
# if num < 0:
#        num = num * (-1)
# if num >= 1 and num <=9:
#        print("el numero tiene 1 digito")
# else:
#        if num >= 10 and num <=99:
#               print("el numero tiene 2 digitos")
#        else:
#               if num >= 100 and num <= 999:
#                      print("el numero tiene 3 digitos")
#               else:
#                      if num >= 1000 and num <= 9999:
#                             print("el numero tiene 4 digitos")
#                      else:
#                             print("el numero tiene mas de 4 digitos")


###*** DECISIONES ANIDADAS

# programa decisiones_anidadas
# variables
#      entero:   n
# inicio
#         escriba "digite un numero entero"   
#         lea num 
#         si num > 0
#                si num >= 10 y num <= 99
#                    escriba "el numero es positivo y tiene dos digitos"
#                sino 
#                    escriba "el numero es positivo y no tiene dos digitos"
#                fin si 
#         sino
#                si num >= -999 y num <= -100
#                     escriba "el numero es negativo y tiene tres digitos"
#                si no 
#                     escriba "el numeo es negativo y no tiene tres digitos"
#                fin si 
#         fin si
               
num = int(input("Por favor, digite un numero entero"))
if num < 0:
       num = num * (-1)
if num >= 10 and num <=99:
       print("el numero es positivo y tiene dos digitos")
else: 
       print("el numero es positivo y no tiene dos digitos")
if num >= -999 and num <= -100:
       print("el numero es negativo y tiene tres digitos")
else:
       print("el numero es negativo y no tiene tres digitos")
                     


       


