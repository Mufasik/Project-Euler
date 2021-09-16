import time
start_time = time.time()

def sum_dig(x):
    t = str(x)
    s = 0
    for i in t:
        s += int(i)
    return s

m = 0
for a in range(11,100):
    for b in range(2,100):
        s = sum_dig(a**b)
        if s > m:
            m = s

print(m)

print("--- %s seconds ---" % (time.time() - start_time))

# 56
"""
Гугол (10**100) - гигантское число: один со ста нулями; 100**100 почти невообразимо велико: один с двумястами нулями. Несмотря на их размер, сумма цифр каждого числа равна всего лишь 1.

Рассматривая натуральные числа вида a**b, где a, b < 100, какая встретится максимальная сумма цифр числа?

972
"""