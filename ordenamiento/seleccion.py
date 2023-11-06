from lista import Lista
from ordenes import *
import random
import time


for i in range(2, 7):
    tiempos = Lista()
    tot_selec = 0
    for _ in range(10):
        lista = Lista()
        print("welta")
        for j in range(10**i):
           lista.insertar(random.randint(0, 10000))
        print("lista generada")

        ini_selec = time.time()
        seleccion(lista)
        fin_selec = time.time()

        t_selec = fin_selec - ini_selec


        tot_selec += t_selec


    prom_selec = tot_selec / 10

    print("promedio:", prom_selec)

