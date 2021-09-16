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

def pan_dig(x):
    T = [str(i) for i in range(10)]
    T[0] = ''
    a = str(x)
    for i in a:
        if T[int(i)] == i:
            T[int(i)] = ''
        else:
            return False
    return True

def change_dig():
    maxi = -1
    for i in range(len(M)-1):
        if M[i]<M[i+1]:
            maxi = i
    maxj = -1
    for j in range(maxi+1,len(M)):
        if M[maxi]<M[j]:
            maxj = j
    M[maxi], M[maxj] = M[maxj], M[maxi]
    # print("mi=",maxi,"mj=",maxj)
    if maxi == -1:
        return False
    N = []
    j = len(M)
    for i in range(j-1,maxi,-1):
        N.append(M[i])
    # print(N)
    for i in range(len(N)):
        M.pop(maxi+1)
        M.append(N[i])
    return True

def uber_check():
    if len(K)<3:
        return False
    for i1 in range(len(K)-2):
        for i2 in range(i1+1,len(K)-1):
            for i3 in range(i2+1,len(K)):
                if K[i2]-K[i1]==K[i3]-K[i2]:
                    print(K[i1],K[i2],K[i3])
                    return True
    return False

N = []
for i in range(1234,9876+1):
    # if pan_dig(i) and simpl(i):
    if simpl(i):
        N.append(i)

lim = 0
for i in N:
    s = str(i)
    M = []
    for j in range(4):
        M.append(int(s[j]))
    K = []
    while True:
        z = ""
        for j in M:
            z += str(j)
        if int(z) in N:
            K.append(int(z))
        if not change_dig():
            break
    # print(K)
    if uber_check():
        lim += 1
    if lim == 2:
        break

print("--- %s seconds ---" % (time.time() - start_time))

# 49
"""
Арифметическая прогрессия: 1487, 4817, 8147, в которой каждый член возрастает на 3330, необычна в двух отношениях: (1) каждый из трех членов является простым числом, (2) все три четырехзначные числа являются перестановками друг друга.

Не существует арифметических прогрессий из трех однозначных, двухзначных и трехзначных простых чисел, демонстрирующих это свойство. Однако, существует еще одна четырехзначная возрастающая арифметическая прогрессия.

Какое 12-значное число образуется, если объединить три члена этой прогрессии?

296962999629
"""