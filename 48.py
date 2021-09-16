import time
start_time = time.time()

def sum_div(x):
    s = 0
    for i in range(1,x+1):
        s += i**i
    return str(s)[-10:]

print(sum_div(1000))

print("--- %s seconds ---" % (time.time() - start_time))

# 48
"""
Сумма 11 + 22 + 33 + ... + 1010 = 10405071317.

Найдите последние десять цифр суммы 11 + 22 + 33 + ... + 10001000.

9110846700
"""