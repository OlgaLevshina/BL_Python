# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
s = input("Введите строку из нескольких слов, разделенных пробелами: ")
l = s.split(" ")
cnt = 1
for i in l:
    print(f"{cnt}. {i[:10:]}")
    cnt = cnt + 1

