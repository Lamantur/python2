a = int(input("введите целое положительное число "))
max = a % 10
while a > 0:

    a = a//10
    if a % 10 > max:
        max = a % 10


print('%s%d' % ("максимальная цифра = ", max))
