# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
# Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой.")
        return

class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашом.")
        return

class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером.")
        return

pen = Pen("Шариковая ручка")
pen.draw()
pencil_1 = Pencil("Цветной карандаш")
pencil_1.draw()
handle_1 = Handle("Спиртовой маркер")
handle_1.draw()

