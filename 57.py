import time
start_time = time.time()

def sqrt2(x):
    m = 0
    top = 1
    bot = 2
    for i in range(1,x):
        top += 2*bot
        top, bot = bot, top
        if len(str(top+bot))>len(str(bot)):
            m += 1
            # print(top+bot,"/",bot)
    print(m)

sqrt2(1000)

print("--- %s seconds ---" % (time.time() - start_time))

# 57
"""
Можно убедиться в том, что квадратный корень из двух можно выразить в виде бесконечно длинной дроби.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

Приблизив это выражение для первых четырех итераций, получим:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

Следующие три приближения: 99/70, 239/169 и 577/408, а восьмое приближение, 1393/985, является первым случаем, в котором количество цифр в числителе превышает количество цифр в знаменателе.

У скольких дробей длина числителя больше длины знаменателя в первой тысяче приближений выражения?

153
"""