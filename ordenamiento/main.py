from lista import Lista
from ordenes import *
import random
import time


for i in range(2, 7):
    tiempos = Lista()
    tot_burbuja = 0
    tot_burbujam = 0
    tot_burbujabi = 0
    tot_selec = 0
    tot_insercion = 0
    tot_quick = 0
    tot_mezcla = 0
    for _ in range(10):
        lista = Lista()
        print("welta")
        for j in range(10**i):
           lista.insertar(random.randint(0, 10000))
        print("lista generada")

        ini_burbuja = time.time()
        burbuja(lista)
        fin_burbuja = time.time()
        print("buble sort termnado")

        ini_burbujam = time.time()
        burbujaMejorada(lista)
        fin_burbujam = time.time()
        print("buble sort m terminado")

        ini_burbujabi = time.time()
        burbujaBidireccional(lista)
        fin_burbujabi = time.time()
        print("buble sort bi terminado")

        ini_selec = time.time()
        seleccion(lista)
        fin_selec = time.time()
        print("seleccion terminado")

        ini_insercion = time.time()
        insercion(lista)
        fin_insercion = time.time()
        print("insercion terminado")

        ini_quick = time.time()
        ordenamientoRapido(lista, 0, lista.get_tamanio() - 1)
        fin_quick = time.time()
        print("quicksort terminado")

        ini_mezcla = time.time()
        ordenamientoMezcla(lista)
        fin_mezcla = time.time()
        print("mezcla terminado")


        t_burbuja = fin_burbuja - ini_burbuja

        t_burbujam = fin_burbujam - ini_burbujam

        t_burbujabi = fin_burbujabi - ini_burbujabi

        t_selec = fin_selec - ini_selec

        t_insercion = fin_insercion - ini_insercion

        t_quick = fin_quick - ini_quick

        t_mezcla = fin_mezcla - ini_mezcla


        tot_burbuja += t_burbuja

        tot_burbujam += t_burbujam

        tot_burbujabi += t_burbujabi

        tot_selec += t_selec

        tot_insercion += t_insercion

        tot_quick += t_quick

        tot_mezcla += t_mezcla

    prom_burbuja = tot_burbuja / 10

    prom_burbujam = tot_burbujam / 10

    prom_burbujabi = tot_burbujabi / 10

    prom_selec = tot_selec / 10

    prom_insercion = tot_insercion / 10

    prom_quick = tot_quick / 10

    prom_mezcla = tot_mezcla / 10

    print(prom_burbuja)
    print("--------------------------------")
    print(prom_burbujam)
    print("--------------------------------")
    print(prom_burbujabi)
    print("--------------------------------")
    print(prom_selec)
    print("--------------------------------")
    print(prom_insercion)
    print("--------------------------------")
    print(prom_quick)
    print("--------------------------------")
    print(prom_mezcla)
