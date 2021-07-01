"""
Escribir un programa qwue pregunte el nombre completo del usuario en consola
y después muestre por pantalla el nombre completo del usuario tres veces,
una con todas la letras minúsculas, otra con todas la letras mayuúsculas
y otra con  la primera letra del nombre y de los apellidos en mayúscula.
El suario puede introducir su nombre combinado mayúsculas como quiera.
"""

nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")

nombre_minusculas = nombre.lower().strip()
nombre_mayusculas = nombre.upper().strip()
nombre_primerletra = nombre.title().strip()

apellido_minusculas = apellido.lower().strip()
apellido_mayusculas = apellido.upper().strip()
apellido_primerletra = apellido.title().strip()

print(f"{nombre} {apellido}", end="\n")
print(f"{nombre_minusculas} {apellido_minusculas}", end="\n")
print(f"{nombre_mayusculas} {apellido_mayusculas}", end="\n")
print(f"{nombre_primerletra} {apellido_primerletra}", end="\n")





