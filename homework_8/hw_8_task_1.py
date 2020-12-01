# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
from datetime import date

class Date:
    def __init__(self, aaa):
        self.aaa = aaa

    def convert_int(self):
        str_lst = self.aaa.split("-")
        try:
            int_lst = [int(x) for x in str_lst]
            return int_lst
        except:
            return print("Введена некорректная дата")

    @staticmethod
    def validate(int_lst):
        try:
            date(int_lst[2], int_lst[1], int_lst[0])
            return print("Введена корректная дата")
        except:
            return print("Введена некорректная дата")

date1 = Date("10-09-2020")
Date.validate(date1.convert_int())
date2 = Date("30-щщ-2020")
Date.validate(date2.convert_int())



