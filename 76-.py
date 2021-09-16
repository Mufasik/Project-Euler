from math import *
import re
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

def nod(a,b):
    return a if b == 0 else nod(b, a % b)

def split_dig(x):
    X = [x]
    total = 1
    print(X)
    while X[0] != 1:
        z = 1
        while X[-1] == 1:
            z += 1
            X.pop()
        X[-1] -= 1
        X.append(z)
        while X[-1] > X[-2]:
            temp = X[-1]
            X[-1] = X[-2]
            X.append(temp-X[-2])
        print(X)
        total += 1
    return total

C = 5

print(split_dig(C))

print("--- %s seconds ---" % (time.time() - start_time))

# 76
"""
Число 5 можно записать в виде суммы ровно шестью различными способами::

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

Сколькими различными способами можно записать число 100 в виде суммы по крайней мере двух целых положительных чисел?
7
6+1
5+2
5+1+1
4+3
4+2+1
4+1+1+1
3+3+1
3+2+2
3+2+1+1
3+1+1+1+1
2+2+2+1
2+2+1+1+1
2+1+1+1+1+1
1+1+1+1+1+1+1

"""
