
def divisores(num):

    divisores = {}
    
    for i in range (1, num + 1):
        divisores[i] = {}
        for x in range(1, i+1):
            if i % x == 0:
                divisores[i].update({x: x==2})
        print(divisores)
        

if __name__ =='__main__':
    rango = int(input("ingrese el rango: " ))
    print(divisores(rango))
    
    multiplos = {i:{x: x*x for x in range(1, i + 1) if i % x == 0} for i in range(1,11)}
    print(multiplos)
    
    