import time
start_time = time.time()
print("--------------------------------------")

def shrink(A, B):
    e = 0
    C = []
    for i in range(len(A)):
        flag = True
        for j in range(len(B)):
            if A[i] == B[j]:
                flag = False
                break
        if flag:
            C.append(A[i])
    # print(C)
    B += C

const = 100

A = []
for i in range(const-1):
    B = []
    for j in range(const-1):
        B.append((i+2)**(j+2))
    A.append(B)

for i in range(1, len(A)):
    shrink(A[i-1], A[i])
    # print(A[i])

print(len(A[const-2]))

print("--- %s seconds ---" % (time.time() - start_time))

# 29 задание

# Рассмотрим все целочисленные комбинации ab для 2 ≤ a ≤ 5 и 2 ≤ b ≤ 5:

# 22=4, 23=8, 24=16, 25=32
# 32=9, 33=27, 34=81, 35=243
# 42=16, 43=64, 44=256, 45=1024
# 52=25, 53=125, 54=625, 55=3125
# Если их расположить в порядке возрастания, исключив повторения, мы получим следующую последовательность из 15 различных членов:

# 4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

# Сколько различных членов имеет последовательность ab для 2 ≤ a ≤ 100 и 2 ≤ b ≤ 100?

# 9183
