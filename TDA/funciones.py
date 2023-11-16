def inicializarPila():
    pila= []
    return pila

def apilar(pila, dato):
    pila.append(dato)
    
def desapilar(pila):
    pila.pop()

def pilaVacia(pila):
    return len(pila)== 0

def tope(pila):
    return pila[-1]

def invertirOrden(pila):
    return pila[::-1]