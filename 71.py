import time
start_time = time.time()

def nod(a,b):
    return a if b == 0 else nod(b, a % b)

def drob_func():
    max_drob = 0
    max_chis = 0
    max_znam = 0
    for znam in range(Z,Z-10,-1):
        # chis = znam // 2
        for chis in range(znam//2,0,-1):
            drob = chis/znam
            if drob < 3/7 and drob > max_drob:
                max_drob = drob
                max_chis = chis
                max_znam = znam
                break
    # print("   3 / 7 =",3/7)
    # print("max_drob =",max_drob)
    # print("nod",nod(max_chis,max_znam))
    print(max_chis)
    # print("max_znam =",max_znam)

Z = 1000000
X = []
drob_func()

print("--- %s seconds ---" % (time.time() - start_time))

# 71
"""
Рассмотрим дробь n/d, где n и d являются положительными целыми числами. Если n<d и НОД(n,d) = 1, то речь идет о сокращенной правильной дроби.

Если перечислить множество сокращенных правильных дробей для d ≤ 8 в порядке возрастания их значений, получим:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

Нетрудно заметить, что дробь 2/5 расположена непосредственно слева от дроби 3/7.

Перечислив множество сокращенных правильных дробей для d ≤ 1 000 000 в порядке возрастания их значений, найдите числитель дроби, расположенной непосредственно слева от дроби 3/7.

428570
"""
