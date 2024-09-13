#Conversión de tipos de datos (Enteros, Decimales y Cadenas).
from pprint import pprint
from statistics import multimode

numero=20
print("\n Inicimos la convercion con un numero entero :",numero)

enteroCadena=str(numero)
print("\n convertimos de entero a cadena ", enteroCadena, type(enteroCadena))


cadenaEntero=int(enteroCadena)
print("\n convertimos de cadena a entero  ", cadenaEntero, type(cadenaEntero))

enteroDecimal=float(cadenaEntero)
print("\n convertimos de entero a decimal ", enteroDecimal, type(enteroDecimal))


# Multilíneas de cadenas Se escribe con triple comilla.

textoMultilinea='''Python es potente... y rápido
funciona bien con otros
funciona en todas partes
es amigable y fácil de aprender
es abierto.'''
print("\n Texto multilinea :",textoMultilinea)

# Función len() Se conoce la longitun de la cadena.
print("\nEl texto multilinea tiene una longitud de: ",len (textoMultilinea), "caracteres")

# Sub cadenas:

# Obtener los primeros n caracteres de una cadena.
primerosN = textoMultilinea[:20]
print("\n Muestran los primeros 20 caracteres: ",primerosN)

# Obtener los caracteres de en medio de una cadena.
mitad=textoMultilinea[50:100]
print("\n Muestra desde el caracter 50 hasta el 100 del texto: ",mitad)

# Obtener los últimos n caracteres de una cadena.
ultimosN = textoMultilinea[-20:]
print("\n Muestan los ultimos 20 caracteres del texto: ",ultimosN)
# Función upper(), se convierte a mayusculas .
print("\n Funcion upper ",textoMultilinea.upper() )
# Función lower(), se convierte el texto a minisculas .
print("\n Funcion lower: ",textoMultilinea.lower() )
#Multilíneas de cadenas de caracteres.
# Función strip() Omite los espacios en blanco de inicio y final del texto .
print(textoMultilinea.strip())
# Función replace()Remplaza las palabras .
texto = "Chanchito Triste"
print(texto)
nuevoTexto=texto.replace("Triste", "Felizzzz")
print(nuevoTexto);
# Función split().
print(nuevoTexto.split())
# Formato de cadenas F-String.
nombre = "Sofia Diaz"
edad = 15
texto_fstring = f"Su nombre es {nombre} y tiene {edad} años."
print(texto_fstring)