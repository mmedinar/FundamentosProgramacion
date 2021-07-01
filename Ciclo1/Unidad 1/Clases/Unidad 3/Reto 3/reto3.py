def reto_3(diccionario: dict) -> str:
    
    if diccionario != None and len(diccionario) == 0:
        mejorpiloto = None
    elif diccionario == None:
        mejorpiloto = None
    else: 
        max_value = max(diccionario.values())

        listOfKeys = list()
        listOfItems = diccionario.items()

        for item  in listOfItems:
            if item[1] == max_value:
                listOfKeys.append(item[0])

        mejorpiloto = ''

        if len(listOfKeys) == 1:
            mejorpiloto = listOfKeys[0]
        else:
            mejorpiloto = ", ".join(listOfKeys)
        
    return mejorpiloto


pilotos = { 'John': 16, 'Alex': 12, 'Bob': 8, 'Mike': 14, 'Molly': 14 }
piloto = reto_3(pilotos)
print("Best: {}".format(piloto))

pilotos = {'John': 12, 'Bob': 14, 'Mike': 16, 'Molly': 16, 'Adam': 10}
piloto = reto_3(pilotos)
print("Best: {}".format(piloto))

pilotos = None
piloto = reto_3(pilotos)
print("Best: {}".format(piloto))

pilotos = {}
piloto = reto_3(pilotos)
print("Best: {}".format(piloto))
