import time
start_time = time.time()

def five_dig(x):
    return x*(3*x-1)//2

C = 3000
X = 3*C*C
M = [1]
F = [False]*X
for i in range(2,C+1):
    t = five_dig(i)
    M.append(t)
    F[t] = True

a,a2,b,b2 = 0,0,0,0
mi = X
for i in range(C-1):
    for j in range(i+1,C):
        p1 = M[i]+M[j]
        p2 = M[j]-M[i]
        if F[p1] and F[p2] and mi>p2:
            mi = p2
            a = M[i]
            a2 = i
            b = M[j]
            b2 = j

print(mi)

print("--- %s seconds ---" % (time.time() - start_time))

# 44
"""
Пятиугольные числа вычисляются по формуле: Pn=n(3n−1)/2. Первые десять пятиугольных чисел:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

Можно убедиться в том, что P4 + P7 = 22 + 70 = 92 = P8. Однако, их разность, 70 − 22 = 48, не является пятиугольным числом.

Найдите пару пятиугольных чисел Pj и Pk, для которых сумма и разность являются пятиугольными числами и значение D = |Pk − Pj| минимально, и дайте значение D в качестве ответа.

5482660
"""