# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше
# предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
from random import randint

a = [randint(0, 40) for i in range(5)]
print(f"Сгенерированный список: {a}")

def my_func(my_list):
    res = []
    i = 0
    while i != len(my_list)-1:
        if my_list[i+1] > my_list[i]:
            res.append(my_list[i+1])
        i = i + 1
    return res
b = my_func(a)
print(f"Отредактированный список: {b}")

