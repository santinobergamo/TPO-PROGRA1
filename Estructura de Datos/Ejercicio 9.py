def tablas (N):
    tabla = {}
    for i in range (1, 13):
        resultado = N * i
        tabla[i] = resultado
    return tabla 

numero = int(input("Ingrese un numero entero para generar la tabla de multiplicar: "))
resultado_tabla = tablas(numero)

print(f"Tabla de multiplicar de {numero}: ")
for clave, valor in resultado_tabla.items():
    print(f"{numero} x {clave} = {valor}")
