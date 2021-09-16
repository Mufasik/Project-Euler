import time
start_time = time.time()

def pifagor3():
    x = 1000
    for a in range(1, x//2):
        for b in range(a, x//2 + 1):
            c = x - a - b
            if c**2 == a**2 + b**2: # and a + b + c == 1000:
                print(a, b, c)
                print(a * b * c)
                break

pifagor3()

print("--- %s seconds ---" % (time.time() - start_time))

# Задача 9
"""
Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство

a2 + b2 = c2
Например, 32 + 42 = 9 + 16 = 25 = 52.

Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.

ответ 31875000

"""
