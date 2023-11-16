def eliminar_comentarios(lineas):
    resultado = []

    for linea in lineas:
        i = 0
        while i < len(linea):
            char = linea[i]

            if char == '#':
                break

            resultado.append(char)

            i += 1

    return ''.join(resultado)

def eliminar_comentarios_archivos(input_file, output_file):
    try:
        with open(input_file, 'r') as archivo_entrada:
            lineas = archivo_entrada.readlines()
    except FileNotFoundError:
        print(f"El archivo no existe: {input_file}")
        return

    contenido_sin_comentarios = eliminar_comentarios(lineas)

    with open(output_file, 'w') as archivo_salida:
        archivo_salida.write(contenido_sin_comentarios)


def main():

    archivo_entrada = 'Archivos/programa_ejemplo.py'
    archivo_salida = 'Archivos/programa_ejemplo_sin_comentarios.py'
    eliminar_comentarios_archivos(archivo_entrada, archivo_salida)
main()
