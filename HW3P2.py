my_list = list(map(str, input('Введите значения через пробел ').split()))
for i in my_list:
    print(f"{my_list.index(i)+1}: {i[:10]}")
# это чтобы не закрывалось окно консоли
    input('Нажмите Enter для выхода\n')
