import time
start_time = time.time()

def five_dig(x):
    return x*(3*x-1)//2

def three_dig(x):
    return x*(x+1)//2

def six_dig(x):
    return x*(2*x-1)

i = 2
j = 2
M = []
N = []
while j>0:
    M.append(six_dig(i))
    a = five_dig(i)
    if a in M:
        N.append(a)
    a = three_dig(i)
    if a in N:
        print(a)
        j -= 1
    i += 1

print("--- %s seconds ---" % (time.time() - start_time))

# 45
"""
Треугольные, пятиугольные и шестиугольные числа вычисляются по нижеследующим формулам:

Треугольные	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Пятиугольные	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Шестиугольные	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
Можно убедиться в том, что T285 = P165 = H143 = 40755.

Найдите следующее треугольное число, являющееся также пятиугольным и шестиугольным.

1533776805
"""