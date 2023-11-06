from lista import Lista


def burbuja(lista):
    for i in range(0, lista.get_tamanio() - 1):
        for j in range(0, lista.get_tamanio() - i - 1):
            if lista.index(j) > lista.index(j + 1):
                aux = lista.index(j)
                lista.reemplazo(j, lista.index(j + 1))
                lista.reemplazo(j + 1, aux)

            #print("Burbuja i[", i, "]-j[", j, "]: vector : ")
            #lista.imprimir()


def burbujaMejorada(lista):
    i = 0
    control = True
    while (i <= lista.get_tamanio() - 2) and control:
        control = False
        for j in range(0, lista.get_tamanio() - i - 1):
            if lista.index(j) > lista.index(j + 1):
                aux = lista.index(j)
                lista.reemplazo(j, lista.index(j + 1))
                lista.reemplazo(j + 1, aux)
                control = True
            #print("Burbuja Mejorada i[", i, "]-j[", j, "]: vector : ")
            #lista.imprimir()
        i = i + 1


def burbujaBidireccional(lista):
    izquierda = 0
    derecha = lista.get_tamanio() - 1
    control = True
    while (izquierda < derecha) and control:
        control = False
        for i in range(izquierda, derecha):
            if lista.index(i) > lista.index(i + 1):
                aux = lista.index(i)
                lista.reemplazo(i, lista.index(i + 1))
                lista.reemplazo(i + 1, aux)
                control = True
            #print(
                "Burbuja Bidireccional f1 izq[",
                i,
                "]-der[",
                derecha,
                "]: vector : ",
            #)
            #lista.imprimir()
        derecha -= 1
        for j in range(derecha, izquierda, -1):
            if lista.index(j) < lista.index(j - 1):
                aux = lista.index(j)
                lista.reemplazo(j, lista.index(j - 1))
                lista.reemplazo(i - 1, aux)
                control = True
            #print(
                "Burbuja Bidireccional f2 izq[",
                izquierda,
                "]-der[",
                j,
                "]: vector : "
            #)
            #lista.imprimir()
        izquierda += 1


def seleccion(lista):
    for i in range(0, lista.get_tamanio() - 1):
        minimo = i
        for j in range(i + 1, lista.get_tamanio()):
            if lista.index(j) < lista.index(minimo):
                minimo = j
            #print(
                "Seleccion i[",
                i,
                "]-j[",
                j,
                "] - minimo(",
                minimo,
                "): vector : "
            #)
            #lista.imprimir()
        aux = lista.index(i)
        lista.reemplazo(i, lista.index(minimo))
        lista.reemplazo(minimo, aux)


def insercion(lista):
    for i in range(1, lista.get_tamanio() + 1):
        k = i - 1
        while (k > 0) and lista.index(k) < lista.index(k - 1):
            aux = lista.index(k)
            lista.reemplazo(k, lista.index(k - 1))
            lista.reemplazo(k - 1, aux)
            #print("Insercion i[", i, "]-k[", k, "]: vector : ")
            #lista.imprimir()
            k -= 1


def ordenamientoRapido(lista, primero, ultimo):
    #print("quickSort:")
    #lista.imprimir()
    izquierda = primero
    derecha = ultimo - 1
    pivote = ultimo
    while izquierda < derecha:
        while lista.index(izquierda) < lista.index(pivote) and izquierda <= derecha:
            izquierda += 1
        while lista.index(derecha) > lista.index(pivote) and derecha >= izquierda:
            derecha -= 1
        if izquierda < derecha:
            aux = lista.index(izquierda)
            lista.reemplazo(izquierda, lista.index(derecha))
            lista.reemplazo(derecha, aux)
    if lista.index(pivote) < lista.index(izquierda):
        aux = lista.index(izquierda)
        lista.reemplazo(izquierda, lista.index(pivote))
        lista.reemplazo(pivote, aux)
    if primero < izquierda:
        ordenamientoRapido(lista, primero, izquierda - 1)
    if ultimo > izquierda:
        ordenamientoRapido(lista, izquierda + 1, ultimo)


def ordenamientoMezcla(lista):
    if lista.get_tamanio() <= 1:
        return lista
    else:
        medio = lista.get_tamanio() // 2
        izquierda = Lista()
        for i in range(0, medio):
            izquierda.insertar(lista.index(i))
        derecha = Lista()
        for i in range(medio, lista.get_tamanio()):
            derecha.insertar(lista.index(i))
        izquierda = ordenamientoMezcla(izquierda)
        derecha = ordenamientoMezcla(derecha)
        if izquierda.index(medio - 1) <= derecha.index(0):
            for i in range(derecha.get_tamanio()):
                izquierda.insertar(derecha.index(i))
            return izquierda
        resultado = mezcla(izquierda, derecha)
        return resultado


def mezcla(izquierda, derecha):
    #print("mergeSort - izq")
    #izquierda.imprimir()
    #print("der")
    #derecha.imprimir()
    lista_mezclada = Lista()
    while izquierda.get_tamanio() > 0 and (derecha.get_tamanio() > 0):
        if izquierda.index(0) < derecha.index(0):
            lista_mezclada.insertar(izquierda.extraer(0))
        else:
            lista_mezclada.insertar(derecha.extraer(0))
    if izquierda.get_tamanio() > 0:
        for i in range(izquierda.get_tamanio()):
            lista_mezclada.insertar(izquierda.index(i))
    if derecha.get_tamanio() > 0:
        for j in range(derecha.get_tamanio()):
            lista_mezclada.insertar(derecha.index(j))
    return lista_mezclada


# lista = [11, 3, 81, 7, 45]
# burbuja(lista)
# print('Burbuja:', lista)

# lista = [11, 3, 81, 7, 45]
# burbujaMejorada(lista)
# print('Burbuja mejorada:', lista)

# lista = [11, 3, 81, 7, 45]
# burbujaBidireccional(lista)
# print('Burbuja bidireccional:', lista)

# lista = [11, 3, 81, 7, 45]
# seleccion(lista)

# lista = [11, 3, 81, 7, 45]
# insercion(lista)

# lista = [11, 3, 81, 7, 45]
# ordenamientoRapido(lista,0,len(lista)-1)

#lista = [11, 3, 81, 7, 45]
#lista = ordenamientoMezcla(lista)
