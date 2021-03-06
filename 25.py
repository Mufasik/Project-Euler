import time
start_time = time.time()
# -------------------------------------------------------


def mul_str(x, y):
    return x + y


elem = 1000
pos = 2
f = 1
t = 1

while f//(10**(elem-1)) == 0:
    f, t = mul_str(f, t), f
    pos += 1
print(pos)

# -------------------------------------------------------
print("--- %s seconds ---" % (time.time() - start_time))

"""
Последовательность Фибоначчи определяется рекурсивным правилом:
Fn = Fn−1 + Fn−2, где F1 = 1 и F2 = 1.
Таким образом, первые 12 членов последовательности равны:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
Двенадцатый член F12 - первый член последовательности, который содержит три цифры.

Каков порядковый номер первого члена последовательности Фибоначчи,
содержащего 1000 цифр?

4782
"""