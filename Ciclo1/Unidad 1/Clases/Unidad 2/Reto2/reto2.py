def reto_2(auto: str, marca: str, modelo: str, año: int, motor: str, potencia: int, 
           disponible: bool, bd_autos: dict) -> dict:
    
    if str(auto).isnumeric() == True:
        resultado = f"Ingrese un id de tipo valido."
    else:
        auto = auto.upper()
        marca = marca.capitalize()
        nombre = modelo.lower()
        año = int(año)
        motor = motor.capitalize()
        caballos = int(potencia)
        resultado = ''
        
        dic_caracteristicas = bd_autos.get(auto)
        
        if dic_caracteristicas != None:
            diferente = False
            
            for key, values in dic_caracteristicas.items():
                
                if key == 'marca':
                    if values != marca: 
                        diferente = True
                        dic_caracteristicas[key] = marca
                if key == 'nombre':
                    if values != nombre: 
                        diferente = True
                        dic_caracteristicas[key] = nombre
                if key == 'año':
                    if values != año: 
                        diferente = True
                        dic_caracteristicas[key] = año
                if key == 'motor':
                    if values != motor: 
                        diferente = True
                        dic_caracteristicas[key] = motor    
                if key == 'caballos':
                    if values != caballos: 
                        diferente = True   
                        dic_caracteristicas[key] = caballos
                if key == 'disponible':
                    if values != disponible: 
                        diferente = True  
                        dic_caracteristicas[key] = disponible
            if diferente == False:
                resultado = (f"El auto {auto} Se encuentra en la base de datos")  
            else:
                resultado = (f"Auto {auto}, actualizado en la base de datos")  
        else:
            Nuevo_carro = {}
            Nuevo_carro['marca'] = marca
            Nuevo_carro['nombre'] = nombre
            Nuevo_carro['año'] = año
            Nuevo_carro['motor'] = motor
            Nuevo_carro['caballos'] = caballos
            Nuevo_carro['disponible'] = disponible
            bd_autos[auto] = Nuevo_carro
            resultado = (f"El auto {auto} se agregó a la base de datos.")  
    
    return resultado       


def bd_autos():
    
    autos = {

        'STARK 01': {
            'marca': 'Ford',
            'nombre': 'flathead roadster',
            'año': 1932,
            'motor': 'V8',
            'caballos': 85,
            'disponible': False
        },
        'STARK 02': {
            'marca': 'Ford',
            'nombre': 'shelby',
            'año': 1967,
            'motor': 'V8',
            'caballos': 427,
            'disponible': False
        },
        'STARK 04': {
            'marca': 'Saleen',
            'nombre': 'S7',
            'año': 2009,
            'motor': 'V8',
            'caballos': 760,
            'disponible': True
        },
        'STARK 12': {
            'marca': 'Tesla',
            'nombre': 'roadster',
            'año': 2009,
            'motor': 'V8',
            'caballos': 292,
            'disponible': False
        },
        'STARK 08': {
            'marca': 'Audi',
            'nombre': 'R8',
            'año': 2008,
            'motor': 'V10',
            'caballos': 525,
            'disponible': True
        }
    }

    return autos


    
autos = bd_autos()
print(reto_2('stark 02', 'ford','SHELBY', 1967, 'v8', 427, False, autos))
print(autos.get('STARK 02', 'Auto no se encuentra en BD.'))

autos = bd_autos()
print(reto_2('stark 04', 'SALEEN','s7', '2009', 'v8', 427, True, autos))
print(autos.get('STARK 04', 'Auto no se encuentra en BD.'))

autos = bd_autos()
print(reto_2(3, 'Rolls-Royce','phanthom', '2002', 'v12', 460, False, autos))
print(autos.get('STARK 03', 'Auto no se encuentra en BD.'))

autos = bd_autos()
print(reto_2('Stark 03', 'Rolls-Royce','phanthom', '2002', 'v12', 460, False, autos))
print(autos.get('STARK 03', 'Auto no se encuentra en BD.'))

