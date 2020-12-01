# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod

class Clothing(ABC):
    @staticmethod
    def total_consumption(clothing_list):
        return sum(el.consumption for el in clothing_list)

    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption() + other.consumption()

class Coat(Clothing):
    def __init__(self, size):
        self.size = size
    @property
    def consumption(self):
        print(f"Расход на пальто {round(self.size / 6.5) + 0.5}")
        return (round(self.size / 6.5) + 0.5)

class Costume(Clothing):
    def __init__(self, growth):
        self.growth = growth

    @property
    def consumption(self):
        print(f"Расход на костюм {(2 * self.growth + 0.3)}")
        return (2 * self.growth + 0.3)

coat_1 = Coat(10)
coat_2 = Coat(20)
cos_1 = Costume(30)
cos_2 = Costume(40)

clothing_list_1 = [coat_1, coat_2, cos_1, cos_2]
print(f"Общий расход ткани: {Clothing.total_consumption(clothing_list_1)}")
