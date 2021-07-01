# for " variable" in "elemento iterable"
#     pass

# for numeros in range(0,11):
#     print(numeros, end= f'\n')

# x = ["manzanas", "peras", "bananas", "melones", "fresas"]
# for i in x:
#     print(i)

# for pares in range(2,101,2):
#     print(pares, end=' ')

# print()

# for i in range(65,91):
#     print(f"{i}{i:c} ", end=' ')

#     #i:c ascci
#     #i:o hexadecimial
#     #i:b binario

# print()
# print(ord('Z'))
# print(chr(90))
#***********************************************
# abcdario = []

# for letra in range(ord('a'), ord('z')+1):
#     #print(letra, sep=' ')
#     abcdario.append(chr(letra))
# print(abcdario)

# vocales = []
# consonantes = []

# for letra in abcdario:
#     if letra in 'aeiou':
#         vocales.append(letra)
#     else:
#         consonantes.append(letra)

# print(vocales)
# print(consonantes)

#***************************************************************************************
# nombres = ['alex','edwin','heynar','galaxy', 'juan']
# profesiones = ['soporte', 'administrador','tecnologo','electricista','ingeniero','ingeniero']

# print(nombres)
# print(profesiones)

# trabajos = {} #{profesion: persona}

# for i in range(len(nombres)):
#     profesion = profesiones[i]
#     persona = nombres[i]
#     if profesion not in trabajos:
#         trabajos[profesion] = [persona]
#     else:
#         trabajos[profesion].append(persona)
#     print(trabajos)

#     input()

# test fizz buzz *********************************************************************
"""
Escribir un programa que muestre en pantalla los números del 1 al 100, sustituyendo
los múltiplos de 3 por la palabra “fizz”, 
los múltiplos de 5 por “buzz” 
y los múltiplos de ambos, es decir, los múltiplos de 3 y 5 (o de 15), por la palabra “fizzbuzz”.
"""
numeros = []

for i in range(1,101):
    if i % 15 == 0:
        valor = "fizzbuzz"
    elif i % 5 == 0:
        valor = "buzz"
    elif i % 3 == 0:
        valor = "fizz"    
    else:
        valor = i
    print(valor, end=' ')

print()
    




