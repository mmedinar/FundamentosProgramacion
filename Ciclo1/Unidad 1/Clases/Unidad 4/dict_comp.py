def square():
    numeros = {}
    
    for i in range (1, 20):
        
        if i%2 != 0:
            numeros[i] = i**2
    
    return numeros

print(square())


def numbers(num1, num2):
    numeros = {}
    for i in range(num1, num2 +1):
        numeros[i] = i**2
    return numeros

numeros_rango = numbers(1,50)
#print(numeros_rango)

def num_div_5(numeros):
    div_5 = {}
    for key in numeros.keys():
        if key % 5 == 0:
            div_5[key] = key**2
    
    return div_5

print(num_div_5(numeros_rango))

        