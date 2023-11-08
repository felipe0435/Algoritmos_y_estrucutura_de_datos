from lista import Lista
from ordenes import *
import random
import time

tiempos = Lista()

for i in range(1, 6):
    tot_mezcla = 0
    for _ in range(10):
        lista = Lista()
        print("welta")
        for j in range(300 * i):
           lista.insertar(random.randint(0, 10000000))
        print("lista generada")

        ini_mezcla = time.time()
        ordenamientoMezcla(lista)
        fin_mezcla = time.time()

        t_mezcla = fin_mezcla - ini_mezcla

        tot_mezcla += t_mezcla

    prom_mezcla = tot_mezcla / 10
    tiempos.insertar(prom_mezcla)
    print("promedio:", prom_mezcla)
tiempos.imprimir()
