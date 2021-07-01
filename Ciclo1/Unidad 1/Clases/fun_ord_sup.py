""" filter """
""" funciones de orden superior  """

def multiplo_5(numero):
    if numero%5 == 0:
        return True
    
numeros = [i for i in range(1,51)]
#print(numeros)

multiplos = filter(multiplo_5, numeros)

#print(multiplos)
#print(list(multiplos))
#print(dict(multiplos))

""" MAP """

def cuadrado(numero):
    return numero**2
        
numeros = [i for i in range(1,6)]
print(numeros)

cuadrados = list(map(cuadrado, numeros))
print(cuadrados)

