def reto_4(diccionario: dict) -> tuple:
    
    if len(diccionario) == 0:
        return None 
    
    dict_valores = diccionario.values()
    
    return dict_valores

pasantes = {'John': {'prueba 1': 8, 'prueba 2': 7, 'prueba 3': 9}, 'Luis': {
'prueba 1': 5, 'prueba 2': 7, 'prueba 3': 9}, 'Ana': {'prueba 1': 6, 'prueba 2': 7, 'prueba 3': 9}}

#print(reto_4(pasantes))


print("ok")
diccionario = pasantes

print(diccionario)
valores = dict(diccionario.values())
print(valores)









# a, b, c, d, e = reto_4(pasantes)
# a = f"Resultados: {a}"
# b = f"Matriz: \n{b}"
# c = f"Promedio: {c}"
# d = f"Puntajes: {d}"
# e = f"Seleccionado: {e}"
# print(a, b, c, d, e, sep='\n')