from lista import Lista
from ordenes import *
import random
import time


tiempos = Lista()
for i in range(1, 6):
    tot_burbujam = 0
    for _ in range(10):
        lista = Lista()
        print("welta")
        for j in range(300 * i):
           lista.insertar(random.randint(0, 10000000))
        print("lista generada")

        ini_burbujam = time.time()
        burbujaMejorada(lista)
        fin_burbujam = time.time()

        t_burbujam = fin_burbujam - ini_burbujam

        tot_burbujam += t_burbujam

    prom_burbujam = tot_burbujam / 10
    tiempos.insertar(prom_burbujam)
    print("promedio:", prom_burbujam)
tiempos.imprimir()
