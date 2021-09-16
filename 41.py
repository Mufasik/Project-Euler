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

def pan_dig_simpl(x):
    T = [str(i) for i in range(10)]
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

M = [1,2,3,4,5,6,7]
m = 1
while True:
    z = ""
    for i in M:
        z += str(i)
    if simpl(int(z)) and int(z)>m:
        m = int(z)
    if not change_dig():
        break
print(m)

print("--- %s seconds ---" % (time.time() - start_time))

# 41
"""
Будем считать n-значное число пан-цифровым, если каждая из цифр от 1 до nиспользуется в нем ровно один раз. К примеру, 2143 является 4-значным пан-цифровым числом, а также простым числом.

Какое существует наибольшее n-значное пан-цифровое простое число?

7652413
"""