from lista import Lista
from ordenes import *
import random
import time


for i in range(2, 7):
    tiempos = Lista()
    tot_burbuja = 0
    for _ in range(10):
        lista = Lista()
        print("welta")
        for j in range(10**i):
           lista.insertar(random.randint(0, 10000))
        print("lista generada")

        ini_burbuja = time.time()
        burbuja(lista)
        fin_burbuja = time.time()

        t_burbuja = fin_burbuja - ini_burbuja
        print(t_burbuja)
        tot_burbuja += t_burbuja

    prom_burbuja = tot_burbuja / 10

    print("promedio:", prom_burbuja)
