# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

try:
    with open("text_hw_5_task_5.txt", "r+") as f_obj:
        numbers = [randint(1, 100) for x in range(10)]
        print(numbers)
        for i in numbers:
            f_obj.write(f"{i} ")
        f_obj.seek(0)
        number = f_obj.read().split()
        summa = 0
        for i in number:
            summa = summa + int(i)
        print(f"Сумма чисел в файле: {summa}")
except IOError:
    print("Произошла ошибка ввода-вывода!")