from funciones import *

def invertir_orden_pila(pila_original):
    pila_invertida = inicializar_pila()
    while not pila_vacia(pila_original):
        apilar(pila_invertida, tope(pila_original))
        desapilar(pila_original)
    return pila_invertida

def main():
    pila = inicializar_pila()
    apilar(pila,17)
    apilar(pila,9)
    apilar(pila,5)
    apilar(pila,24)
    pila_resultante = invertir_orden_pila(pila)
    print(pila_resultante)
main()





