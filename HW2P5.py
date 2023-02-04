my_list = list(map(str, input('Введите значения через пробел ').split()))
for i in my_list:
    if (len(i) > 10):
        print('%s' % (i[:10]))
        continue
    print(i)
