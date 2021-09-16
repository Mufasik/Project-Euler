from math import sqrt
import time
start_time = time.time()
print("--------------------------------------")

def simpl(x):
    for i in range(3, round(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


def count_simpl(x, y):
    z = 0
    while z**2+x*z+y > 0 and simpl(z**2+x*z+y):
        z += 1
    return z

C = 1000
t = am = bm = 0
nm = 1

for a in range(-C+1, C):
    for b in range(-C, C+1):
        t = count_simpl(a, b)
        if t > nm:
            nm = t
            am = a
            bm = b

print(am*bm)

print("--- %s seconds ---" % (time.time() - start_time))

# 26
"""
n^2+an+b, где |a|<1000 и |b|≤1000

Найдите произведение коэффициентов a и b квадратичного выражения, согласно которому можно получить максимальное количество простых чисел для последовательных значений n, начиная со значения n=0.
Ответ: -59231

"""