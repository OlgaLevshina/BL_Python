# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
# должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
def int_func(slovo):
    res = slovo.capitalize()
    return res

print(int_func('test'))

stroka = "iz slov, razdelennix probelom"
l = stroka.split(" ")
i = 0
for elem in l:
    l[i] = int_func(elem)
    i = i + 1
stroka = " ".join(l)
print(stroka)
