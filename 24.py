import time

start_time = time.time()
# -------------------------------------------------------

TEMP = [str(i) for i in range(10)]


def find(num, A):
    for n in A:
        if n == num:
            return True
    return False

def gen_num(N, M, prefix=None):
    prefix = prefix or []
    global T
    if M == 0:
        T += 1
        if T == 1000000:
            print(prefix)
        return
    for digit in range(N):
        if find(digit, prefix):
            continue
        prefix.append(digit)
        gen_num(N, M - 1, prefix)
        prefix.pop()

T = 0
gen_num(10, 10)
# print(T)

# -------------------------------------------------------
print("--- %s seconds ---" % (time.time() - start_time))

"""Перестановка - это упорядоченная выборка объектов. К примеру, 3124 является одной из возможных перестановок из цифр 1, 2, 3 и 4. Если все перестановки приведены в порядке возрастания или алфавитном порядке, то такой порядок будем называть словарным. Словарные перестановки из цифр 0, 1 и 2 представлены ниже:

012   021   102   120   201   210

Какова миллионная словарная перестановка из цифр 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9?"""

# 2783915460