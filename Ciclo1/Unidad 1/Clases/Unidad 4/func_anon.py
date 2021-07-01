""" OPeradores encadenados """

menor = 1 <2 and 2 < 3
print (menor)

menor_2 = 1 < 2 < 3
print(menor_2)

mayor = 3 > 2 > 1
print(mayor)


""" Comprobar si un número se encuentra entre 0 y 100 """
numero = 30
if numero >=0 and numero <= 100:
    print(f"El número {numero} se encuentra entre 0 y 100")
else:
    print(f"El número {numero} no se encuentre entre 0 y 100")
    


""" Funcion Anónima """

def cuadrado(numero):
    return numero * numero
    
print(cuadrado(5))

numero_cuadrado = lambda num: num**2
print(numero_cuadrado(5))

""" palindromo """
def palindromo_func(palabra):
    return palabra == palabra[::-1]

print(palindromo_func("ana"))

palindromo2 = lambda palabra: palabra == palabra[::-1]
print(palindromo2("ana"))

""" impar """
impar = lambda num: num%2 != 0
print(impar(5))


""" revertir """
revertir = lambda palabra: palabra[::-1]
print(revertir("MarioFernando"))
    
suma = lambda x,y: x+y
print(suma(2,5))
    
