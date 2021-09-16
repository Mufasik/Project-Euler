import time
start_time = time.time()

def good_check(x):
    X = []
    s = str(x*2)
    for i in s:
        X.append(i)
    X.sort()
    for j in range(3,7):
        s = str(x*j)
        T = []
        for i in s:
            T.append(i)
        T.sort()
        # print(T)
        if T != X:
            return False
    return True

i = 10
while True:
    if good_check(i):
        print(i)
        break
    i += 1

print("--- %s seconds ---" % (time.time() - start_time))

# 52
"""
Найдите такое наименьшее положительное целое число x, чтобы 2x, 3x, 4x, 5x и 6x состояли из одних и тех же цифр.

142857
"""