#trabajo algoritmos 1
import time
import random
import algoritmos1
import pandas as pd

# generar una lista de tamaño n
def generarL(n):
    nums = []
    valores = random.randint(1, 10)
    for i in range(n):
        nums.append(valores)
        valores += random.randint(1, 5)
    target = random.choice(nums) + random.choice(nums)
    
    return (nums, target)

# medir el tiempo de ejecución
def medir_time(algoritmo, n):
    t1 = time.time_ns()
    x = generarL(n)
    algoritmo(x[0], x[1])
    t2 = time.time_ns()
    t = t2-t1
    if t < 500:
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
    
    return t    

def main():
    i = 0
    p1 = []
    p2 =[]
    values = []
    n = 100
    while i != 7:
        values.append(n)
        p1.append(medir_time(algoritmos1.searchpairswithlists, n))
        p2.append(medir_time(algoritmos1.searchpairswithsets, n))
        i += 1
        n = 2*n
    datos_finales_p1 = pd.DataFrame({"n": values, "Time(ns)": p1})
    datos_finales_p2 = pd.DataFrame({"n": values, "Time(ns)": p2})

    print("\tMetodo de Listas:\n",datos_finales_p1)
    print("\tMetodo de Conjuntos:\n", datos_finales_p2)


if __name__ == "__main__":
    main()