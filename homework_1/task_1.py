# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

a_int = 10
b_float = 5.5
c_str = "homework_1"
d_bool = True
print(a_int, b_float, c_str, d_bool)
print(type(a_int), type(b_float), type(c_str), type(d_bool))

i1 = input("Введите целое число ")
print(i1, type(i1))

i2 = input("Введите вещественное число ")
print(i2, type(i2))

i3 = input("Введите строку ")
print(i3, type(i3))

print("Что бы вы не ввели, все равно тип будет str!")
