from lista import Lista
from ordenes import *
import random
import time


for i in range(2, 7):
    tiempos = Lista()
    tot_burbujam = 0
    for _ in range(10):
        lista = Lista()
        print("welta")
        for j in range(10**i):
           lista.insertar(random.randint(0, 10000))
        print("lista generada")

        ini_burbujam = time.time()
        burbujaMejorada(lista)
        fin_burbujam = time.time()

        t_burbujam = fin_burbujam - ini_burbujam

        tot_burbujam += t_burbujam

    prom_burbujam = tot_burbujam / 10

    print("promedio:", prom_burbujam)
