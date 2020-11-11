# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк. '''

second = str()
while second.isdigit() == False:
    second = input("Введите время в секундах ")
second = int(second)
h = second//3600
m = (second % 3600)//60
s = (second % 3600) % 60
second = f"{h:02}:{m:02}:{s:02}"
print(second)
