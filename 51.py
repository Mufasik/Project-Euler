from math import sqrt
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

def create_mask(x):
    m = str(x)
    z = m[:-1]
    Z = [i for i in z]
    Z_ = [i for i in z]
    Z__ = ["*" for i in z]
    while True:
        for i in range(len(Z)):
            if Z[i] == "*":
                Z[i] = Z_[i]
            else:
                Z[i] = "*"
                mask = ""
                for j in Z:
                    mask += j
                mask += m[-1]
                # print(mask)
                if count_simpl_mask(mask) == Q:
                    # print(mask)
                    return True
                break
        if Z == Z__:
            break
    return False

def count_simpl_mask(m):
    count = 0
    i = 0
    if m[0]=="*":
        i += 1
    A = []
    while i<10:
        x = m.replace("*",str(i))
        A.append(x)
        if simpl(int(x)):
            count += 1
        if count == Q:
            print(A[0])
        i += 1
    return count

C = 6
Q = 8
S = []
for i in range(10**C//10,10**C):
    if simpl(i):
        S.append(i)

i = 0
while True:
    if create_mask(S[i]):
        break
    i += 1
    if i >= len(S):
        break

print("--- %s seconds ---" % (time.time() - start_time))

# 51
"""
Меняя первую цифру числа *3 (двузначного числа, заканчивающегося цифрой 3), оказывается, что шесть из девяти возможных значений - 13, 23, 43, 53, 73 и 83 - являются простыми числами.

При замене третьей и четвертой цифры числа 56**3 одинаковыми цифрами, получаются десять чисел, из которых семь - простые: 56003, 56113, 56333, 56443, 56663, 56773 и 56993

Найдите наименьшее простое число, которое является одним из восьми простых чисел, полученных заменой части цифр (не обязательно соседних) одинаковыми цифрами.

121313
"""