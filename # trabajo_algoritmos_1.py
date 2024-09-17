# trabajo algoritmos 1
import time
import random

# generar una lista de tamaño n
def generarL(n):
    nums = []
    valores = random.randint(1, 10)
    for i in range(n):
        nums.append(valores)
        valores += random.randint(1, 5)
    target = random.choice(nums) + random.choice(nums)
    
    return nums, target

# medir el tiempo de ejecución
def medir_time(algoritmo, x: 0, y: 0):
    t1 = time.time_ns
    algoritmo(x, y)
    t2 = time.time_ns
     t = t2 - t1
        if t < 500:
            k = 100
            t1 = time.time_ns
            while i != k:
                x = medir(n)
                algoritmo(x[0], x[1])
                i += 1
            t2 = time.time_ns
            T1 = t2 - t1
            t1 = time.time_ns
            while i != k:
                x = medir(x)
                i += 1
            t2 = time.time_ns
            T2 = t2 - t1
    
            t = (T2 - T1)/k
        
        return t
