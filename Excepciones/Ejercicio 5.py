import math

def main():
    try:
        num = float(input("Ingrese un numero mayor a 0: "))
        res = math.sqrt(num)
        print("La raiz cuadrada de ",num, "es: ",res)
        
    except ValueError:
        print("Error, se esperaba un numero mayor a 0.")
main()
        
