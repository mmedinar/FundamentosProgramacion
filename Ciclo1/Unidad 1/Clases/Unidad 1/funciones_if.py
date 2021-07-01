#clase 2021-05-11
#Anotaciones  --> sirve para dar información al codigo


def saludar(nombre: str) -> None:
    print("Hola " + nombre)


#estudiante = saludar("Mario")

def sumar(num1: int, num2: int) -> int:
    return num1 + num2

#print(sumar(2,3))


def positivo_negativo(num: int) -> str:
    if num > 0:
        out = f'{num} es mayor que 0'
    elif num == 0:
        out = f'{num} es igual que 0'
    else:
        out = f'{num} es manor que 0'
    
    return out


numero = positivo_negativo(-12)

#print(numero)


"""
- 'El último digito de NUMERO es DIGITO' -->CONDICIONES:
   - Si el digito es mayor que 5:  ' y es mayor que cinco '
   - si el digito es 0: 'y es cero'
   - si el digito es menor que 6: ' y es menor que 6 y no es 0'

   se utiliza la funcion modulo para conocer el ultimo digito   % 10, o %100 para los 2 ultimos digitos
"""

def ultimo_digito(num: int) -> str:
    import math
    
    ultimo =  int(str(abs(num))[-1])
    if ultimo > 5:
        out = f'{ultimo} es mayor que 5'
    elif ultimo == 0:
        out = f'{ultimo} y es 0'
    else: 
        out = f'{ultimo} y es menor que 6 y no es 0'

    out = f'\n El último digito de {num} es ' + out + '\n'

    return out
 

import random
numero = random.randint(-10000, 10000)
print(ultimo_digito(numero))
 

""""
 -  bebe = 0 - 4
 - niños = 5 - 13
 - adolescentes = 14 - 17
 - adulto joven = 18 - 35
 - adultos = 36 - 64
 - tercera edad = 65 - ....
 """

rangos = ["bebe","niño","adoloscente", "adulto joven","adulto","tercera edad"]
edad_usuario = int(input("Ingrese su edad: "))

def etapa_edad(edad: str, etapas: list) -> str:

    if edad <= 4:
        idx = 0
        #print(etapas[0])
    elif edad <= 13:
        idx = 1
        #print(etapas[1])
    elif edad <= 17:
        idx = 2
        #print(etapas[2])
    elif edad <= 35:
        idx = 3
        #print(etapas[3])
    elif edad <= 64:
        idx = 4
        #print(etapas[4])
    else: 
        idx = 5
        #print(etapas[-1])

    return None

etapa_edad(edad_usuario, rangos)

