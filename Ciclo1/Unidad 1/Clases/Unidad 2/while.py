#contar numeros

# a = 1
# print(a)

# a += 1
# #print(a)

# while a <= 10:
#     print(a)
#     a += 1

# var_1 = 1
# var_2 = 5

# while a !=-1:
#     a = int(input('Ingrese la opción: '))

#     if a == 1:
#         print(f'{var_1} + {var_2} = {var_1 + var_2}')
#     elif a == 2:
#         print(f'{var_1} - {var_2} = {var_1 - var_2}')
#     elif a == 3:
#         print(f'{var_1} / {var_2} = {var_1 / var_2}')
#     elif a == 4:
#         print(f'{var_1} * {var_2} = {var_1 * var_2}')

# numero = 1

# while numero <= 10:
#     print(numero)
#     numero  += 1

    
n = 1
pares = []
impares = []

while n <= 20:
    if n % 2 != 0:
        impares.append(n)
        # input()
    else:
        pares.append(n)
        # input()
    n += 1

print(pares)
print (impares)
    
