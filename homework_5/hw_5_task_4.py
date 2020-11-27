# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
numbers = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
try:
    with open("text_hw_5_task_4.txt", "r") as f_obj:
        for line in f_obj:
            number = line.split()
            number[0] = numbers.get(number[0])
            number = (' '.join(number))
            with open("text_hw_5_task_4_itog.txt", "a") as f_obj_itog:
                f_obj_itog.write(f"{number}\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")

