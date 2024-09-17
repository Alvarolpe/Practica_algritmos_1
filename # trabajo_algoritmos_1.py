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

    return t2 - t1    