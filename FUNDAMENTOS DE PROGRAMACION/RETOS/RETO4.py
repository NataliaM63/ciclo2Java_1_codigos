def procesar_frase(frase_celebre_programacion: str) -> dict:
    diccionario = {}
    to_remove = ["'", '"', ",", ".", ";", "(", ")", "/", "\n"]
    for i in to_remove:
        frase_celebre_programacion = frase_celebre_programacion.replace(i, "")
    lista_de_palabras = frase_celebre_programacion.split()
    
    for i in lista_de_palabras:
        repetido = lista_de_palabras.count(i)
        if repetido > 1:
            diccionario[i] = repetido
    return diccionario

print(procesar_frase('depurar codigo es dos veces mas dificil que escribir codigo, por lo tanto, si escribes el codigo tan inteligentemente como'))














