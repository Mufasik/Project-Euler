from math import sqrt
import time
start_time = time.time()

def simp(x):
    if x == 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    f = round(sqrt(x)+1)
    for i in range(3, f, 2):
        if x % i == 0:
            return False
    return True

m, n , k = 10001, 2, 1
while n <= m:
    k += 2
    if simp(k):
        n += 1
        # print(k, end=" ")
print(k)
# время 0.2 (ответ 104743) - перебором


# --------------------------------------------------------------------------------------------------------------------
print("--- %s seconds ---" % (time.time() - start_time))

# Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13.
# Очевидно, что 6-ое простое число - 13.
#
# Какое число является 10001-ым простым числом?

# 104743
