# 4. Реализуйте базовый класс Car. У данного класса должы быть следующие атрибуты:
# # speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# # которые должны сообщать, что машина понехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала.")
        return

    def stop(self):
        print(f"Машина {self.name} остановилась.")
        return

    def turn(self, direction):
        print(f"Машина {self.name} повернула {direction}.")
        return

    def show_speed(self):
        print(f"Скорость машины {self.name} составляет {self.speed} км/ч.")
        return

class TownCar(Car):
    def __init__(self, speed, color, name, is_police, place):
        super().__init__(speed, color, name,is_police)
        self.is_police = False
        self.place = place

    def show_speed(self):
        if self.speed > 60:
            print("ВНИМАНИЕ, нарушение скоростного режима!")
        print(f"Скорость машины {self.name} составляет {self.speed} км/ч.")
        return


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, work):
        super().__init__(speed, color, name,is_police)
        self.is_police = False
        self.work = work

    def show_speed(self):
        if self.speed > 40:
            print("ВНИМАНИЕ, нарушение скоростного режима!")
        super(WorkCar, self).show_speed()
        return

class SportCar(Car):
    def __init__(self, speed, color, name, is_police, power):
        super().__init__(speed, color, name,is_police)
        self.is_police = False
        self.work = power

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = True

towncar_1 = TownCar(59, "red", "KIA", True, 4)
print(towncar_1.is_police)
towncar_1.show_speed()

workcar_1 = WorkCar(45, "green", "Автобус", True, "Рейсовый автобус")
workcar_1.show_speed()

sportcar_1 = SportCar(350, "yellow", "Ferrari", False, 660)
sportcar_1.go()
sportcar_1.show_speed()
sportcar_1.stop()
sportcar_1.turn("налево")
sportcar_1.show_speed()

policecar_1 = PoliceCar(50, "blue", "ДПС", True)
policecar_1.go()
policecar_1.turn("направо")
policecar_1.show_speed()
policecar_1.stop()
policecar_1.show_speed()
