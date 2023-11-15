# Recursividad

# Ejercicio 8

def ordenar_seleccion_recursiva(lista):
    
    if len(lista) <= 1:                                                  # Caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
        return lista

    indice_minimo = lista.index(min(lista))                              # Encuentra el índice del elemento más pequeño en la lista
    lista[0], lista[indice_minimo] = lista[indice_minimo], lista[0]      # Intercambia el elemento más pequeño con el primero
    resto_ordenado = ordenar_seleccion_recursiva(lista[1:])              # Llamada recursiva para ordenar el resto de la lista
    
    return [lista[0]] + resto_ordenado                                   # Combina el primer elemento y el resto ordenado


# Ejemplo del programa
lista_numeros = [5, 2, 8, 1, 3]
lista_ordenada = ordenar_seleccion_recursiva(lista_numeros)
print("Lista original:", lista_numeros)
print("Lista ordenada:", lista_ordenada)
