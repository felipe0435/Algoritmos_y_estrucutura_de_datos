from lista import Lista
from ordenes import *
import random
import time

tiempos = Lista()

for i in range(3, 9):
    tot_burbujabi = 0
    for _ in range(10):
        lista = Lista()
        print("welta")
        for j in range(2**i):
           lista.insertar(random.randint(0, 10000000))
        print("lista generada")

        ini_burbujabi = time.time()
        burbujaBidireccional(lista)
        fin_burbujabi = time.time()

        t_burbujabi = fin_burbujabi - ini_burbujabi
        print(t_burbujabi)
        tot_burbujabi += t_burbujabi

    prom_burbujabi = tot_burbujabi / 10
    tiempos.insertar(prom_burbujabi)
    print("promedio:", prom_burbujabi)
tiempos.imprimir()

