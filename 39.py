import time
start_time = time.time()

def P_count_pifagor(x):
    rezult = 0
    for a in range(1, x//2):
        for b in range(a, x//2 + 1):
            c = x - a - b
            if c**2 == a**2 + b**2:
                rezult += 1
                # print(a, b, c)
    return rezult
# C = 100000000

max_result = 1
for i in range(840, 841):
    temp = P_count_pifagor(i)
    if temp > max_result:
        max_result = temp
        t = i

print(t)

print("--- %s seconds ---" % (time.time() - start_time))

# 39
"""
Если p - периметр прямоугольного треугольника с целочисленными длинами сторон {a,b,c}, то существует ровно три решения для p = 120:

{20,48,52}, {24,45,51}, {30,40,50}

Какое значение p ≤ 1000 дает максимальное число решений?
Ответ: 840
"""