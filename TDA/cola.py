def inicializar_cola():
    cola=[]
    return cola

def acolar(cola, dato):
    cola.append(dato)
    
def desacolar(cola):
    cola.pop(0)
    
def primero(cola):
    return cola[0]

def cola_vacia(cola):
    return len(cola)==0