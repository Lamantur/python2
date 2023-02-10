my_list = [7, 5, 3, 3, 2]
new_list = my_list
m = int(input("введите новое число  >>> "))
for i in my_list:
    if m > i:
        new_list.insert(new_list.index(i), m)
        break
    else:
        new_list.append(m)
        break
print(new_list)
