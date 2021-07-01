string = str()
lista = list()
tupla = tuple()
diccionario = dict()

print('' == string, lista, tupla, diccionario, sep= '\n')

diccionario = {} #{key: value}

datos = {"nombre": "Mario",
         "apellido": "Medina",
         "universidad": "UTP",
         "Curso": "Python"
        }

llaves = datos.keys()
valores = datos.values()

print(llaves, valores, sep='\n')

print(datos["universidad"])

