def uno_a_100():
    numeros = []
    
    for i in range(1,101):
        numeros.append(i)
        
    return numeros

numeros = [i for i in range(1,101)]


alfabeto = [chr(i) for i in range(ord('a'), ord('z') + 1)]
#print(alfabeto)

def square(lista):
    cuadrado = []
    
    for num in lista:
        cuadrado.append(num * num)
        
    return cuadrado

#print(square(numeros))

cuadrados = [i * i for i in numeros]
#print(cuadrados)


def div_3(numeros):
    div = []
    
    for i in numeros:
        if i % 3  == 0:
            div.append(i)
    
    return div


print(div_3(numeros))
    
divisibles_por_3 = [i for i in numeros if i % 3 == 0]
print(divisibles_por_3)


#cudrado de numeros pares que están entre 1 y 10
numeros_2 = [i**2 for i in range(1,11) if i % 2 == 0]
print(numeros_2)