def seguridad():
    '''Devuelve True si se ingresa una contraseña de forma correcta en un maximo de 3 intentos.'''
    contraseña = 'boca+grande' # Colocar contraseña
    intentos = 0
    salida = False
    while intentos < 3:
        intentos += 1
        ingreso = input("Constraseña: ")
        if contraseña == ingreso:
            salida = True
            break
        print("Contraseña incorrecta")
    else:
        print("Se alcanzó el maximo de intentos (3)")
    return salida


