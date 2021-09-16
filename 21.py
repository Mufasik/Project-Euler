import time
start_time = time.time()

const = 10000

def delit(x):
    summa = 1
    for j in range(2, x//2+1):
        if x % j == 0:
            summa += j
    return summa

A = [0, 0]
B = []
for i in range(2, const):
    A.append(delit(i))
# print(A[284])

for i in range(2, len(A)):
    temp = A[i]
    if i < temp < const and i == A[temp]:
        # print(i, temp)
        B.append(i)
        B.append(temp)

# print(B)
print(sum(B))

print("--- %s seconds ---" % (time.time() - start_time))

# d(n) сумма делителей n (<n делят n нацело)
# d(a) = b
# d(b) = a
# a != b
# a и b - друж
#
# Например, делителями числа 220 являются
# 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110,
# поэтому d(220) = 284.
# Делители 284 - 1, 2, 4, 71, 142,
# поэтому d(284) = 220.
#
# Подсчитайте сумму всех дружественных чисел меньше 10000.

# 31626