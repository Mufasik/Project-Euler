import time
start_time = time.time()

const = 1

def polindrom(x):
    t = str(x)
    for c in range(len(t)//2):
        if t[c] != t[len(t)-c-1]:
            return False
    return True
    
max = 111111
for i in range(100,1000):
    for k in range(i, 1000):
        if polindrom(i*k) and i*k > max:
            # print(i, k, i*k)
            max = i*k

print(max)

print("--- %s seconds ---" % (time.time() - start_time))



# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

# 906609













