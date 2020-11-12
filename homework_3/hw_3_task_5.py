# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к
# уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

def sum_numbers(num_list):
    total_sum = 0
    for i in num_list:
        total_sum = total_sum + i
    return total_sum
sum_total = 0
while True:
    str_list = input("Введите последовательность чисел через пробел: ").lower()
    str_list = str_list.split(" ")
    if str_list.count('') > 0:
        while str_list.count('') != 0:
            str_list.remove('')
    if str_list.count('q') > 0:
        while str_list.count('q') != 0:
            str_list.remove('q')
        int_list = [int(x) for x in str_list]
        sum_total = sum_total + sum_numbers(int_list)
        print(f"Сумма введенных чисел: {sum_total}")
        int_list = []
        break
    else:
        int_list = [int(x) for x in str_list]
        sum_total = sum_total + sum_numbers(int_list)
        print(f"Сумма введенных чисел: {sum_total}")
        int_list = []