from arbol import nodoArbol
from lista import Lista
from ordenes import *
import time
import random


tiempos = Lista()

for i in range(3, 8):
    tot_arbol = 0
    lista = Lista()
    for _ in range(10):
        print("welta")
        for _ in range(2**i):
            lista.insertar(random.randint(0, 10000000))
        print("lista generada")

        ini_arbol = time.time()
        arbol = nodoArbol(lista.index(0))
        for j in range(1, lista.get_tamanio()):
            arbol.insertarNodo(lista.index(j))
        fin_arbol = time.time()

        t_arbol = fin_arbol - ini_arbol

        tot_arbol += t_arbol

    prom_arbol = tot_arbol / 10
    tiempos.insertar(prom_arbol)
    print("promedio:", prom_arbol)
tiempos.imprimir()
