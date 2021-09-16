import time
start_time = time.time()
print("--------------------------------------")

def polindrom(x):
    t = str(x)
    for c in range(len(t)//2):
        if t[c] != t[len(t)-c-1]:
            return False
    return True

def polindrom_v2(x):
    x_ = x
    if x % 2 == 0:
        return False
    z = ""
    while x//2 > 0:
        if x % 2 != 0:
            z += "1"
        else:
            z += "0"
        x //= 2
        # print(z)
    z += "1"
    # print(z)
    return polindrom(x_) and polindrom(z)

C = 1000000
S = 0

for i in range(1,C):
    if polindrom_v2(i):
        # print(i)
        S += i

print(S)

print("--- %s seconds ---" % (time.time() - start_time))

# 36
"""
 Десятичное число 585 = 1001001001 v2 (в двоичной системе), является палиндромом по обоим основаниям.

Найдите сумму всех чисел меньше миллиона, являющихся палиндромами по основаниям 10 и 2.

(Пожалуйста, обратите внимание на то, что палиндромы не могут начинаться с нуля ни в одном из оснований).

Ответ: 872187
"""