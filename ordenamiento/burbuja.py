from lista import Lista
from ordenes import *
import random
import time


tiempos = Lista()
for i in range(1, 6):
    tot_burbuja = 0
    for _ in range(10):
        lista = Lista()
        print("welta")
        for j in range(300*i):
           lista.insertar(random.randint(0, 10000000))
        print("lista generada")

        ini_burbuja = time.time()
        burbuja(lista)
        fin_burbuja = time.time()

        t_burbuja = fin_burbuja - ini_burbuja
        print(t_burbuja)
        tot_burbuja += t_burbuja

    prom_burbuja = tot_burbuja / 10
    tiempos.insertar(prom_burbuja)
    print("promedio:", prom_burbuja)

tiempos.imprimir()
