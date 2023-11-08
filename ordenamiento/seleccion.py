from lista import Lista
from ordenes import *
import random
import time

tiempos = Lista()

for i in range(3, 9):
    tot_selec = 0
    for _ in range(10):
        lista = Lista()
        print("welta")
        for j in range(2**i):
           lista.insertar(random.randint(0, 10000000))
        print("lista generada")

        ini_selec = time.time()
        seleccion(lista)
        fin_selec = time.time()

        t_selec = fin_selec - ini_selec


        tot_selec += t_selec


    prom_selec = tot_selec / 10
    tiempos.insertar(prom_selec)
    print("promedio:", prom_selec)
tiempos.imprimir()

