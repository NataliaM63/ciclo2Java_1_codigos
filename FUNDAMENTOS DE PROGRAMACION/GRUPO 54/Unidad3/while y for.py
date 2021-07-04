###*** WHILE -> Mientras que 

# n = 5
# while n > 0:
#     print(n)
#     n = n - 1
# print('Despegue!')


# def factorial(n: int) -> int:
#     resultado = 1
#     numero_actual = 2
#     while numero_actual <= n:     ###(CONDICION)
#     # while not numero_actual > n:   ###(TAMBIEN SE PUEDE ESCRIBIR)
#         resultado = resultado * numero_actual
#         numero_actual += 1    ###(INCREMENTO -> Por que es suma)
#     return resultado

# print(factorial(5))

# resultado = 1 y numero_actual = 2 
# resultado * numero_actual
# (1*2=3)(2*3=6)(6*4=24)(24*5=120)

###*** ERRORES 

#"ESTE ES UN CICLO INFINITO Y TEMINE HASTA QUE SE DETENGA EL PROGRAMA O SE DAÑE LA MEMORIA DEL COMPUTADOR"
#*"PARA DETENER LA EJECUCION (CTRL+C"

# i = 1
# while i > 0:
#     print(i)
#     i = i + 1
# print("termine")

# i = 1
# while i < 10:
#     print(i)
# i = i + 1
# print("termine")

###*** BUCLE "WHILE" CONTROLADO POR EVENTO

# promedio, total, contar = 0.0, 0, 0

# print("Introduzca la nota de un estudiante (-1 para salir): ")
# grado = int(input())
# while grado != -1:
#     total = total + grado
#     contar = contar + 1
#     print("Introduzca la nota de un estudiante (-1 para salir): ")
#     grado = int(input())
# promedio = total / contar
# print("promedio de notas del grado escolar es: " + str(promedio))

###*** BUCLE "WHILE" CON "ELSE"

# promedio, total, contar = 0.0, 0, 0
# mensaje = "Introduzca la nota de un estudiante (-1 para salir): "

# grado = int(input(mensaje))
# while grado != -1:
#     total = total + grado
#     contar += 1
#     grado = int(input(mensaje))
# else:
#     promedio = total / contar
#     print("Promedio de notas del grado escolar: " + str(promedio))

## SENTENCIA BREAK 
# variable = 10
# while variable > 0:
#     print('Actual valor de variable:', variable)
#     variable = variable - 1 
#     if variable == 5:
#         break

# variable = 10
# while variable > 0:
#     variable = variable - 1 
#     if variable == 5:
#         continue   ###(no imprime lo qur hay de bajo)
#     print('Actual valor de variable:', variable)
    
###*** EJEMPLOS 
##"SUCESION DE FIBONACCI --> suma"
#(este imprime hasta el 100)

# a, b = 0, 1 
# while b < 100:
#     print(b)
#     a, b = b, a + b


###*** FOR 
# for x in range(1, 3):   ###(5, 13)
#     print("estamos en la iteracion " + str(x))

# for j in range(0, 10 , 2):
#     print("estamos en la iteracion " + str(j))

# for j in range(10, 0 , -2):
#     print("estamos en la iteracion " + str(j))

# oracion = 'Mary entiende muy bien python'
# frases = oracion.split()    ## CONVIERTE A UNA LISTA CADA PALABRA
# print("La oracion analizada es:", oracion, ".\n")
# print(frases)

##.split("se puede utilizar cualquier palabra")
# oracion = 'Mary entiende muy bien python'
# frases = oracion.split('e')    ## CONVIERTE A UNA LISTA CADA PALABRA
# print("La oracion analizada es:", oracion, ".\n")
# print(frases)

# oracion = 'Mary entiende muy bien python'
# frases = oracion.split()    ## CONVIERTE A UNA LISTA CADA PALABRA
# print("La oracion analizada es:", oracion, ".\n")
# print(frases)
# for palabra in range(len(frases)):
#     print("palabra: {0}, en la frases su posicion es: {1}".format(
#         frases[palabra], palabra))
###*** nombres, apellidos, etc. -> (clave)
###*** Leonardo, Caballero,etc. -> todo despues de los dos puntos(:)(valor)

# datos_basicos = {
#     "nombres":"Leonardo Jose",
#     "apellidos":"Caballero Garcia",
#     "cedula":"26938401",
#     "fecha_nacimiento":"03/12/1980",
#     "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
#     "nacionalidad":"Venezolana",
#     "estado_civil":"Soltero"
# }
# clave = datos_basicos.keys()
# valor = datos_basicos.values()

# cantidad_datos = datos_basicos.items()

# for clave, valor in cantidad_datos:
#     print(clave + ": " + valor)
# print(clave + ": " + valor)

# for c in clave:
#     print(c)

# frutas = {'Fresa':'roja', 'Limon':'verde', 'Papaya':'naranja', 'Manzana':'amarilla', 'Guayaba':'rosa'}
# for nombre, color in frutas.items():
#     print(nombre, "es de color", color)

# frutas = {'Fresa':'roja', 'Limon':'verde', 'Papaya':'naranja', 'Manzana':'amarilla', 'Guayaba':'rosa'}
# for llave in frutas:
#     print(llave, 'es de color', frutas[llave])

    ###***BUCLE "FOR" CON "ELSE"

db_connection = "127.0.0.1", "5432", "root", "nomina"

for parametro in db_connection:
    print(parametro)
else:print("""El comando postgrSQL es:
           $ psql -h {server} -p {port} -u {user} - d {db_name}""".format(server=db_connection[0], port=db_connection[1],
                                                                          user=db_connection[2], db_name=db_connection[3]))








