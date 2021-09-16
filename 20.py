import time
start_time = time.time()

def fact(x):
    temp = 1
    for i in range(x):
        temp *= i + 1
    return temp

z = str(fact(100))
# print(z)
t = 0
for k in z:
    t += int(k)

print(t)

print("--- %s seconds ---" % (time.time() - start_time))

# n! означает n × (n − 1) × ... × 3 × 2 × 1

# Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Найдите сумму цифр в числе 100!.

# 648