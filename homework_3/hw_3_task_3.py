# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func(a, b, c, *args):
    l = []
    l = sorted([a, b, c, *args])
    res = l[len(l)-1] + l[len(l)-2]
    return res
print(my_func(16,1,4))
