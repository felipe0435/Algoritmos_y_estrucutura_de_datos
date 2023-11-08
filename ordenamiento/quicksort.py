from lista import Lista
from ordenes import *
import random
import time

tiempos = Lista()

for i in range(3, 10):
    tot_quick = 0
    for _ in range(10):
        lista = Lista()
        print("welta")
        for j in range(2**i):
           lista.insertar(random.randint(0, 10000000))
        print("lista generada")

        ini_quick = time.time()
        ordenamientoRapido(lista, 0, lista.get_tamanio() - 1)
        fin_quick = time.time()

        t_quick = fin_quick - ini_quick

        tot_quick += t_quick

    prom_quick = tot_quick / 10
    tiempos.insertar(prom_quick)
    print("promedio", prom_quick)
tiempos.imprimir()
