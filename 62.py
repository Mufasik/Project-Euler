import time
start_time = time.time()

def same_dig(x,y):
    return sorted(str(x)) == sorted(str(y))

C = 5 #5
M = 10000
Z = [i**3 for i in range(M//2,M)]
j = 0
k = 1
while k<C:
    X = []
    X.append(Z[j])
    k = 1
    for i in range(j+1,len(Z)):
        if same_dig(X[0],Z[i]):
            X.append(Z[i])
            k += 1
            # print(X)
    j += 1
    if j == len(Z)-1:
        break

# print(k)
print(X[0])

print("--- %s seconds ---" % (time.time() - start_time))

# 62
"""
Можно найти перестановки куба 41063625 (345**3), чтобы получить еще два куба: 56623104 (384**3) и 66430125 (405**3). К слову, 41063625 является наименьшим кубом, для которого ровно три перестановки также являются кубами

Найдите наименьший куб, для которого ровно пять перестановок также являются кубами.

127035954683
"""

