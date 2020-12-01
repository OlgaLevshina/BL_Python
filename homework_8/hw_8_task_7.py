# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение
# созданных экземпляров. Проверьте корректность полученного результата.
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print("Сумма комплексных чисел:")
        return Complex(self.a + other.a, self.b + other.b)

    def __str__(self):
        return f"{self.a} + {self.b}i"

    def __mul__(self, other):
        print("Произведение комплексных чисел:")
        return Complex(self.a*other.a - self.b*other.b, self.a*other.b + self.b*other.a)

com_1 = Complex(5, 10)
com_2 = Complex(6, 4)
print(com_1)
print(com_2)
print(com_1+com_2)
print(com_1*com_2)
