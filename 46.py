from math import sqrt
import time
start_time = time.time()

def simpl(x):
    if x == 2 or x == 3:
        return True
    elif x % 2 == 0 or x == 1:
        return False
    for i in range(3, round(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def sum_sq(x):
    for i in range(1,round(sqrt(x//2))+1):
        z = x-(2*(i**2))
        if z>0 and simpl(z):
            # print(x,"=",z,"+2*",i,"^2")
            return True
    return False

i = 9
while True:
    if not simpl(i) and not sum_sq(i):
        print(i)
        break
    i += 2

print("--- %s seconds ---" % (time.time() - start_time))

# 46
"""
Кристиан Гольдбах показал, что любое нечетное составное число можно записать в виде суммы простого числа и удвоенного квадрата.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

Оказалось, что данная гипотеза неверна.

Каково наименьшее нечетное составное число, которое нельзя записать в виде суммы простого числа и удвоенного квадрата?

5777
"""