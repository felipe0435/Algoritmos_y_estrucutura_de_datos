from lista import Lista
from ordenes import *
import random
import time


for i in range(2, 7):
    tiempos = Lista()
    tot_quick = 0
    for _ in range(10):
        lista = Lista()
        print("welta")
        for j in range(10**i):
           lista.insertar(random.randint(0, 10000))
        print("lista generada")

        ini_quick = time.time()
        ordenamientoRapido(lista, 0, lista.get_tamanio() - 1)
        fin_quick = time.time()

        t_quick = fin_quick - ini_quick

        tot_quick += t_quick

    prom_quick = tot_quick / 10

    print("promedio", prom_quick)
