from lista import Lista
from ordenes import *
import random
import time


for i in range(2, 7):
    tiempos = Lista()
    tot_mezcla = 0
    for _ in range(10):
        lista = Lista()
        print("welta")
        for j in range(10**i):
           lista.insertar(random.randint(0, 10000))
        print("lista generada")

        ini_mezcla = time.time()
        ordenamientoMezcla(lista)
        fin_mezcla = time.time()

        t_mezcla = fin_mezcla - ini_mezcla

        tot_mezcla += t_mezcla

    prom_mezcla = tot_mezcla / 10

    print("promedio:", prom_mezcla)
