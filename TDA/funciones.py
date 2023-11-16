def inicializar_pila():
    pila= []
    return pila

def apilar(pila, dato):
    pila.append(dato)
    
def desapilar(pila):
    pila.pop()

def pila_vacia(pila):
    return len(pila)== 0

def tope(pila):
    return pila[-1]

def invertir_orden(pila):
    return pila[::-1]
