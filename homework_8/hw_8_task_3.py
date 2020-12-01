# # 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# # Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# # Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
# соответствующее сообщение. При этом работа скрипта не должна завершаться.

class NewException(Exception):
    def __init__(self, txt):
        self.txt = txt

list_numbers = []
while True:
    inp_data = input("Введите число (для завершения введите stop): ")
    if inp_data == "stop":
        print(list_numbers)
        break
    else:
        try:
            if inp_data.isdigit() == False:
                raise NewException("Вы ввели не число")
        except NewException as err:
            print(type(err), err)
        else:
            inp_data = int(inp_data)
            list_numbers.append(inp_data)
            print(f"Все хорошо, мы добавили число {inp_data} в список.")