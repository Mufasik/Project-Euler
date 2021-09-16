from math import sqrt
import time
start_time = time.time()
# print()

def simpl(x):
    if x == 2 or x == 3:
        return True
    elif x % 2 == 0 or x == 1:
        return False
    for i in range(3, round(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def uber_simpl(x):
    zl = str(x)
    zr = str(x)
    if not simpl(x):
        return False
    while len(zl) > 1:
        zl = zl[1:]
        zr = zr[:-1]
        # print(zl, zr)
        if not simpl(int(zl)) or not simpl(int(zr)):
            return False
    return True

C = 1000000
S = 0
for i in range(11, C):
    if uber_simpl(i):
        # print(i)
        S += i

print(S)
# print(uber_simpl(i))

print("--- %s seconds ---" % (time.time() - start_time))

# 37
"""
Число 3797 обладает интересным свойством. Будучи само по себе простым числом, из него можно последовательно выбрасывать цифры слева направо, число же при этом остается простым на каждом этапе: 3797, 797, 97, 7. Точно таким же способом можно выбрасывать цифры справа налево: 3797, 379, 37, 3.

Найдите сумму единственных одиннадцати простых чисел, из которых можно выбрасывать цифры как справа налево, так и слева направо, но числа при этом остаются простыми.

ПРИМЕЧАНИЕ: числа 2, 3, 5 и 7 таковыми не считаются.
Ответ: 748317
"""