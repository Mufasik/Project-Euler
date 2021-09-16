import time
start_time = time.time()
print("--------------------------------------")

def uber_fact(x):
    z = str(x)
    c = 0
    for i in z:
        c += F[int(i)]
    if c == x:
        return True
    else:
        return False

C = 1000000
F = [1, 1]
for i in range(2, 10):
    F.append(F[i-1]*i)

print(F)
sum = 0
for i in range(3, C):
    if uber_fact(i):
        sum += i
        print(sum)

# print(sum)

print("--- %s seconds ---" % (time.time() - start_time))

# 34
"""
145 является любопытным числом, поскольку 1! + 4! + 5! = 1 + 24 + 120 = 145.

Найдите сумму всех чисел, каждое из которых равно сумме факториалов своих цифр.

Примечание: поскольку 1! = 1 и 2! = 2 не являются суммами, учитывать их не следует.

Ответ: 40730

"""