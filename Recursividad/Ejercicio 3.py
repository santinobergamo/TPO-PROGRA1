def suma(N):
    if N <= 0:
        return 0
    else:
        return N + suma(N-1)
resultado = suma(6)
print(resultado )
