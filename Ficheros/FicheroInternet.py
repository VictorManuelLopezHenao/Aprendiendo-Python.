import requests #sirve para hacer solicitudes HTTP, o sea, conectarte con sitios web, APIs, o archivos en internet de forma muy sencilla.

print("\nAcceso a un fichero de internet")

url = input("\nDigite la URL del fichero: ")

respuesta = requests.get(url)  # Descargar el contenido del fichero desde la URL
respuesta.raise_for_status()  # Verificar si hubo algún error en la solicitud

contenido = respuesta.text     # Obtener el contenido del fichero como texto


palabras = contenido.split()
num_palabras = len(palabras)

print(f"\nEl fichero contiene {num_palabras} palabras")
