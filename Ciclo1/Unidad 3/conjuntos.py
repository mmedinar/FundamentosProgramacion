

conjunto = set(range(1,5))
#print(conjunto)

s = {1, 2, 3, 4, 5}
b = {True, "Python", 2, 3.1416, (7, 10)}

#print(s)
#print(b)

s1 = {1, 2, 3, 4, 5, 6, 5}
#print(s1)

repetidos = {1,2,2,5,"hola","hola", (7,10), (7,10), (10,7)}
#print(repetidos)

#for i in repetidos:
#    print(i)
    
"""operador UNION""" 
union = s | b
#print(union)

"""operador INTERSECCION""" 
interseccion = s & b
#print(interseccion)


"""operador DIFERENCIA """
diferencia_s_b = s - b
diferencia_b_s = b - s
#print(diferencia_b_s)
#print(diferencia_s_b)

"""operador DIFERENCIA SIMETRICA ^"""
#simetrica_a = s ^ b
#simetrica_b = b ^ s
#print(simetrica_a)
#print(simetrica_b)


"""OPERADORES REALACIONALES"""
conjunto1 = {1,2,3,4}
conjunto2 = {3,4,5,6}
conjunto3 = {4,3,2,1}

#print(conjunto1 == conjunto3)
#print(conjunto1 != conjunto2)
#print(conjunto1 > conjunto3)
#print(conjunto1 > conjunto2)
#print(conjunto1 >= conjunto3)
#print(conjunto1 > conjunto2)

"""FUNCIONES"""
conjunto1 = {1,2,3,4}
#print(len(conjunto1))
#print(max(conjunto1))
#print(min(conjunto1))
#print(sum(conjunto1))


"""METODOS"""
c = {1,2,3,4}
c.add(5)
c.remove(3)
print(c)
c.discard(1)
print(c)
c.pop()
print(c)

conjunto = {12, "python", 32.21, 7}
for dato in conjunto:
    if dato == 7:
        print(f"Tenemos el dato {dato} en el conjunto")
        

