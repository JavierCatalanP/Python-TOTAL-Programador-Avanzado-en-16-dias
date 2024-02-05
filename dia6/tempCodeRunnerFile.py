def sobrescribir(ruta_archivo):
    try:
        # Abre el archivo en modo escritura ('w') para sobrescribir el contenido
        with open(ruta_archivo, 'w') as archivo:
            # Sobrescribe el contenido del archivo con el texto "contenido eliminado"
            archivo.write("contenido eliminado")
        return f"El archivo {ruta_archivo} ha sido sobrescrito con éxito."
    except FileNotFoundError:
        # Captura la excepción si el archivo no se encuentra
        return f"El archivo {ruta_archivo} no fue encontrado."
    except Exception as e:
        # Captura cualquier otra excepción no anticipada
        return f"Ocurrió un error al sobrescribir el archivo: {e}"

# Ejemplo de uso
ruta_del_archivo = "ruta/del/archivo.txt"  # Reemplaza con la ruta y nombre de tu archivo
resultado = sobrescribir(ruta_del_archivo)

print(resultado)