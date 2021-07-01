"""
escribir un programa que almacene en una lista 
los números del 1 al 10
y los muestre por pantalla en
orden inverso separados por comas
"""

numero = list(range(1,11))
print(numero)

print(numero[::-1])


#import random as rd
#desorden = rd.randrange(1,15,stop=False) #.randint(1,15)


desorden = [3, 2,6,4,8,3,9,7,8]
print(desorden)
desorden.sort(reverse=True)
print(desorden)
desorden.sort()
print(desorden)

desorden.reverse()
print(desorden)



