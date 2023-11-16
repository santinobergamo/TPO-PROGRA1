def domino (ficha_1, ficha_2):
    return ficha_1[1] == ficha_2[0] or ficha_1[0] == ficha_2[1]

def main():
    valor_1_1 = int(input("Ingrese el primer valor de la ficha 1: "))
    valor_1_2 = int(input("Ingrese el segundo valor de la ficha 1: "))
    ficha_1 = (valor_1_1, valor_1_2)
    valor_2_1 = int(input("Ingrese el primer valor de la ficha 2: "))
    valor_2_2 = int(input("Ingrese el segundo valor de la ficha 2: "))
    ficha_2 = (valor_2_1, valor_2_2)
    resultado = domino(ficha_1, ficha_2)
    print(resultado )
main()
