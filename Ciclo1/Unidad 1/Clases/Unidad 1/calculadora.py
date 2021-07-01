import funciones_calc as calc


def calculadora(num1: int, num2: int, operacion: str) -> int:
    if operacion == '+':
        result = calc.suma(num1, num2)
    elif operacion == '-':
        result = calc.resta(num1, num2)
    elif operacion == '/':
        if num2 != 0:
            result = calc.division(num1, num2)
        else:
            result = 'Division por 0 no está definida'
    elif operacion == '*':
        result = calc.multiplicacion(num1, num2)

    return result

caculo = calculadora(5,1,'/')
print(caculo)