# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class NewException(Exception):
    def __init__(self, text):
        self.text = text

def division(a, b):
    if not b:
        raise NewException("Делить на 0 нельзя")
    return a / b

try:
    print(division(100, 0))
except NewException as err:
    print(type(err), err)

try:
    print(division(100, 10))
except NewException as err:
    print(type(err), err)

