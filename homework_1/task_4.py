# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.'''
n = str()
while n.isdigit() == False:
    n = input("Введите положительное число n ")
n = int(n)
big = 0
while n % 10 != 0:
    a = n % 10
    if big < a:
        big = a
        n = n//10
    else:
        n = n//10
print("Самая большая цифра: " + str(big))

