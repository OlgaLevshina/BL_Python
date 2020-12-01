# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

#Описание класса Склад
class Warehouse:
    __inventory = {}

    def __str__(self):
        return str(self.__inventory)

    def put_equipment(self, equipment):
        equipment.department = "Warehouse"
        equipment_type = equipment.get_type()
        ls = self.__inventory.get(equipment_type) or []
        ls.append(equipment)
        self.__inventory[equipment_type] = ls

    def get_equipment(self):
        pass

#Описание класса Департамент
class Department:
    pass

#Описание класса базового класса Оргтехника
class Office_Eguipment:
    department = ""
    def __init__(self, id_equip, manufacture, speed, max_format):
        self.id_equip = id_equip
        self.manufacture = manufacture
        self.speed = speed
        self.max_format = max_format

    @classmethod
    def get_type(cls):
        return cls.__name__

#Описание класса-наследника Принтер
class Printer(Office_Eguipment):
    def __init__(self, id_equip, manufacture, speed, max_format, print_tech):
        super().__init__(id_equip, manufacture, speed, max_format)
        self.print_tech = print_tech

#Описание класса-наследника Сканер
class Scanner(Office_Eguipment):
    def __init__(self, id_equip, manufacture, speed, max_format, type_sc):
        super().__init__(id_equip, manufacture, speed, max_format)
        self.type_sc = type_sc

#Описание класса-наследника Копировальный аппарат
class Copy(Office_Eguipment):
    def __init__(self, id_equip, manufacture, speed, max_format, color_copy):
        super().__init__(id_equip, manufacture, speed, max_format)
        self.color_copy = color_copy

my_wh = Warehouse()
printer_1 = Printer('P001', 'Canon', '50', 'A2', 'лазерная')
printer_2 = Printer('P002', 'HP', '100', 'A1', 'светодиодная')
printer_3 = Printer('P003', 'HP', '70', 'A5', 'термо')
scanner_1 = Scanner('S001', 'Epson', '30', 'A4', '3D')
scanner_2 = Scanner('S002', 'Epson', '25', 'A3', 'ручной')
scanner_3 = Scanner('S003', 'Epson', '40', 'A4', 'планшетный')
copy_1 = Copy('C001', 'KYOCERA', '80', 'A4', True)
copy_2 = Copy('C002', 'Lexmark', '80', 'A4', False)
copy_3 = Copy('C003', 'Epson', '80', 'A4', True)

my_wh.put_equipment(printer_1)
my_wh.put_equipment(printer_2)
my_wh.put_equipment(printer_3)
my_wh.put_equipment(scanner_1)
my_wh.put_equipment(scanner_2)
my_wh.put_equipment(scanner_3)
my_wh.put_equipment(copy_1)
my_wh.put_equipment(copy_2)
my_wh.put_equipment(copy_3)
print(my_wh)



