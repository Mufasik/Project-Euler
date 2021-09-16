from math import sqrt
import re
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

A = 1
step = 2
count = 1
count_s = 0

while True:
    for i in range(4):
        A += step
        if simpl(A):
            count_s += 1
        count += 1
        # print(A)
    # print("spiralka =",step+1)
    step += 2
    if count_s/count*100 < 10:
        # print(count_s,count,count_s/count*100)
        print(step-1)
        break

print("--- %s seconds ---" % (time.time() - start_time))

# 58
"""
Начиная с 1 и продвигаясь по спирали в направлении против часовой стрелки, получается квадратная спираль с длиной стороны 7

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

Интересно заметить, что нечетные квадраты лежат на правой нижней полудиагонали. Еще интереснее то, что среди 13 чисел, лежащих на обеих диагоналях, 8 являются простыми; т.е. отношение составляет 8/13 ≈ 62%.
какой будет длина стороны квадратной спирали, у которой отношение количества простых чисел к количеству всех чисел на обеих диагоналях упадет ниже 10%

26241
"""