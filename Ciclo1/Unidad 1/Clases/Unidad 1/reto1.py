
def reto1(t1: str, f1: float, b1: int, g1: float, t2: str, f2: float, b2: int, g2: float) -> str:
    horasTallerFabricacion = float(240)
    horasTallerBarniz = float(200)

    m2tipo1 = horasTallerBarniz * f2 - horasTallerFabricacion * (b2/60)
    m2tipo1 = m2tipo1 / ((b1/60)*f2 - f1*(b2/60))
    m2tipo1 = int(m2tipo1)

    m2tipo2 = horasTallerFabricacion - m2tipo1 * f1
    m2tipo2 = m2tipo2 / f2
    m2tipo2 = int(m2tipo2)


    ganancia1 = m2tipo1 * g1
    ganancia2 = m2tipo2 * g2/3500
    ganancia = int(ganancia1) + int(ganancia2)
    ganancia = float(ganancia)

    tipo = f"Tipo {t1}: {m2tipo1} m2, Tipo {t2}: {m2tipo2} m2, Ganancia: {ganancia} USD"
    return tipo


 #   #“Tipo {t1}: {tipo1} m2, Tipo {t2}: {tipo2} m2, Ganancia:”


print(reto1("A", 0.3, 12, 4, "B", 0.2, 12, 10500))
print(reto1("C", 0.4, 24, 5, "D", 0.2, 9, 14000))
print(reto1("X", 0.2, 6, 7, "Y", 0.4, 30, 7000))

    #m22tipo2 = int(horasTallerBarniz - m2tipo1 * (b1/60))/(b2/60)
    #ganancia22 = ganancia1 + (m22tipo2 * g2/3500)


#t1, t2 - Carácter del tipo de lámina
#f1, f2 - Tiempo en horas en el taller de fabricación, valor
#decimal entre 0.1 y 1.0
#b1, b2 - Tiempo en minutos en el taller de fabricación,
##valor entero entre 1 y 30
#g1 - Ganancia del producto en USD, valor decimal
#mayor a 0
##g2 - Ganancia del producto en cop, valor decimal
#mayor a 0
