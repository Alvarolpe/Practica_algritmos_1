#trabajo algoritmos 1
# Álvaro López Pérez: alvaro.lopez.perez@udc.es
# Luca Grygar Casas: luca.grygarc@udc.es

import time
import random
import algoritmos1
import pandas as pd
import numpy as np

# generar una lista de tamaño n
def generarL(n):
    '''
    Genera una lista aleatoria ordenada de 
    números enteros ordenada de tamaño n
    y un número que sea la suma de dos de 
    sus elementos

    Parameters
    ----------
    n : TYPE
        DESCRIPTION. 
        Número de elementos de la lista

    Returns
    
    -------
    nums : TYPE
        DESCRIPTION.
        lista de números
    target : TYPE
        DESCRIPTION.
        suma de dos elementos

    '''
    nums = []
    valores = random.randint(1, 10)
    for i in range(n):
        nums.append(valores)
        valores += random.randint(1, 5)
    target = random.choice(nums) + random.choice(nums)
    
    return (nums, target)

# medir el tiempo de ejecución
def medir_time_100(algoritmo, n):
    '''
    Evalúa el tiempo que tarda en ejecutarse 
    un algoritmo dado
    con k=100 (repeticiones por defecto)

    Parameters
    ----------
    algoritmo : TYPE
                func
        DESCRIPTION.
        Algoritmo a evaluar
    n : TYPE
        int
        DESCRIPTION.
        número de elementos que tendrá la 
        lista con la que se evaluará el algoritmo

    Returns
    -------
    t : TYPE
        float
        DESCRIPTION.
        tiempo en el que se realizó 
    A : TYPE
        bool
        DESCRIPTION.
        si se supera el umbral de tiempo en una llamada 
        al algoritmo es false

    '''
    A = False
    t1 = time.time_ns()
    x = generarL(n)
    algoritmo(x[0], x[1])
    t2 = time.time_ns()
    t = t2-t1
    if t < 500:
        A = True
        i = 0
        k = 100
        t1 = time.time_ns()
        while i != k:
            x = generarL(n)
            algoritmo(x[0], x[1])
            i += 1
        t2 = time.time_ns()
        T1 = t2 - t1
        t1 = time.time_ns()
        while i != k:
            x = generarL(x)
            i += 1
        t2 = time.time_ns()
        T2 = t2-t1

        t = (T1-T2)/k
    
    return (t, A)

def medir_time_1000(algoritmo, n):
    '''
    Evalúa el tiempo que tarda en ejecutarse 
    un algoritmo dado
    con k=1000 (repeticiones por defecto)

    Parameters
    ----------
    algoritmo : TYPE
                func
        DESCRIPTION.
        Algoritmo a evaluar
    n : TYPE
        int
        DESCRIPTION.
        número de elementos que tendrá la 
        lista con la que se evaluará el algoritmo

    Returns
    -------
    t : TYPE
        float
        DESCRIPTION.
        tiempo en el que se realizó
    A : TYPE
        bool
        DESCRIPTION.
        si se supera el umbral de tiempo en una llamada 
        al algoritmo es false

    '''
    A = False
    t1 = time.time_ns()
    x = generarL(n)
    algoritmo(x[0], x[1])
    t2 = time.time_ns()
    t = t2-t1
    if t < 500:
        A = True
        i = 0
        k = 1000
        t1 = time.time_ns()
        while i != k:
            x = generarL(n)
            algoritmo(x[0], x[1])
            i += 1
        t2 = time.time_ns()
        T1 = t2 - t1
        t1 = time.time_ns()
        while i != k:
            x = generarL(x)
            i += 1
        t2 = time.time_ns()
        T2 = t2-t1

        t = (T1-T2)/k
    
    return (t, A)

def main():
    '''
    Crea la tabla de las mediciones y la muestra

    Returns
    -------
    None.

    '''
    i = 0
    f1 = []
    f2 =[]
    a1 = []
    a2 = []
    values = []
    n = 100
    while i != 7:
        values.append(n)
        m1 = medir_time_100(algoritmos1.searchpairswithlists, n)
        m2 = medir_time_1000(algoritmos1.searchpairswithsets, n)
        f1.append(m1[0])
        a1.append(m2[1])
        f2.append(m2[0])
        a2.append(m2[1])
        i += 1
        n = 2*n
    datos_finales_f1 = pd.DataFrame({"n": values, "Avarage": a1, "Time(ns)": f1})
    datos_finales_f2 = pd.DataFrame({"n": values, "Avarage": a2, "Time(ns)": f2})

    n1 = datos_finales_f1["n"]
    t1 = datos_finales_f1["Time(ns)"]
    datos_finales_f1["t(n)/O(nlog2(n))"] = t1/(n1*np.log2(n1))
    datos_finales_f1["t(n)/O(n^2)"] = t1/(n1**2)
    datos_finales_f1["t(n)/O(n^2.3)"] = t1/(n1**2.3)

    n2 = datos_finales_f2["n"]
    t2 = datos_finales_f2["Time(ns)"]
    datos_finales_f2["t(n)/O(log2(n))"] = t2/np.log2(n2)
    datos_finales_f2["t(n)/O(n)"] = t2/n2
    datos_finales_f2["t(n)/O(n^1.2)"] = t2/ (n2**1.2)

    print("\tMetodo de Listas:\n",datos_finales_f1, "\n\n")
    print("\tMetodo de Conjuntos:\n", datos_finales_f2)

if __name__ == "__main__":
    main()
