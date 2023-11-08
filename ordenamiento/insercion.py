from lista import Lista
from ordenes import *
import random
import time

tiempos = Lista()

for i in range(3, 11):
    tot_insercion = 0
    for _ in range(10):
        lista = Lista()
        print("welta")
        for j in range(2**i):
           lista.insertar(random.randint(0, 10000000))
        print("lista generada")

        ini_insercion = time.time()
        insercion(lista)
        fin_insercion = time.time()

        t_insercion = fin_insercion - ini_insercion

        tot_insercion += t_insercion

    prom_insercion = tot_insercion / 10
    tiempos.insertar(prom_insercion)
    print("promedio:", prom_insercion)
tiempos.imprimir()
