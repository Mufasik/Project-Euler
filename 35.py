from math import sqrt
import time
start_time = time.time()
print("--------------------------------------")

def simpl(x):
    if x == 2 or x == 3:
        return True
    elif x % 2 == 0:
        return False
    for i in range(3, round(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

C = 1000000
S = [False]*C

for i in range(5, C, 2):
    S[i] = simpl(i)
# print(S)

def combo_digit_simpl(x):
    z = str(x)
    for i in z:
        z = z[1:]
        z += i
        # print(z)
        if not S[int(z)]: #simpl(int(z)):
            return False
    return True

sim = 2 #2,3

for i in range(5, C, 2):
    if combo_digit_simpl(i):
        # print(i)
        sim += 1

print(sim)
# print(combo_digit_simpl(23))

print("--- %s seconds ---" % (time.time() - start_time))

# 35
"""
Число 197 называется круговым простым числом, потому что все перестановки его цифр с конца в начало являются простыми числами: 197, 719 и 971.

Существует тринадцать таких простых чисел меньше 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97.

Сколько существует круговых простых чисел меньше миллиона?
Ответ: 55
"""