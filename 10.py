import time
start_time = time.time()

M = 2000000

simps = [True] * M

for i in range(4, M, 2):
    simps[i] = False

i = 3
while i**2 < M:
    if simps[i]:
        for j in range(i**2, M, i):
            simps[j] = False
    i += 1

sim = [x for x in range(2, M) if simps[x]]

print(sum(sim))

print("--- %s seconds ---" % (time.time() - start_time))

# Задача 10
"""
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше двух миллионов.

ответ 142913828922
"""
