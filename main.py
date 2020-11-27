# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

# import time
# class Traffic_Light:
#     __color: str
#
#     def traffic_lighter_runing(self):
#         __color = 'Red'
#         print(f"Цвет светофора: {__color}")
#         time.sleep(7)
#         __color = 'Yellow'
#         print(f"Цвет светофора: {__color}")
#         time.sleep(2)
#         __color = 'green'
#         print(f"Цвет светофора: {__color}")
#         time.sleep(6)
#
# tr_l = Traffic_Light()
#
# tr_l.traffic_lighter_runing()

# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т
#
#
# class Road:
#     _length: int
#     _width: int
#     asphalt_kgs: int
#     sm_req: int
#     def slozhny_method_asfalta(self,_length, _width, asphalt_kgs = 25, sm_req = 5):
#         result_of_calc = _width*_length*asphalt_kgs*sm_req
#         print(result_of_calc)
#
# rrr = Road()
#
# rrr.slozhny_method_asfalta(20, 5000)



# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
#
# class Worker:
#     #name: str
#     name = 'Eric'
#     #surname: str
#     surname = 'Cartman'
#     position = "Bastard"
#     _income = {"wage": 5000, "bonus": 666}
#
# class Position(Worker):
#
#
#     def get_full_name(self):
#
#         return f"{Worker.name} {Worker.surname}"
#
#     def get_total_income(self):
#
#         return sum(Worker._income.values())
#         pass
#
#
# aaa = Position()
# print(aaa.get_full_name())
#
# print(aaa.get_total_income())
#





# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# class Car:
#     speed: int
#     color: str
#     name: str
#     is_police: bool
#
#     def method_go(self):
#         return "the vehicle has stared moving"
#         pass
#
#     def method_stop(self):
#         return 'the vehicle has stopped'
#         pass
#
#     def method_turn(self, orientation = 'straight'):
#         return f"the vehicle has turned {orientation}"
#         pass
#
#     def show_speed(self, speed = 666):
#         return speed
#
# class TownCar(Car):
#     def show_speed(self, speed = 666):
#         if speed > 60:
#             print("You are busted")
#
#     pass
#
#
# class SportCar(Car):
#     pass
#
# class WorkCar(Car):
#     def show_speed(self, speed = 666):
#         if speed > 40:
#             print("You are busted")
#         else:
#             print("drive safely")
#
#
# class PoliceCar(Car):
#     pass
#
#
#
# carobject = Car()
# #print(carobject.show_speed(),carobject.method_turn())
# wor_c = WorkCar()
#
# #print(wor_c.show_speed(666))
#
# town_o = TownCar()
#
# print(town_o.show_speed())


# 5. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

# Я так понимаю задание реализовано в предыдущих?

# 6. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str

    def meth_draw(self):
        print("“Запуск отрисовки.”")

class Pen(Stationery):

    def meth_draw(self, title = 'pen'):
        print(f"“Запуск отрисовки. ”{title}")
    pass

class Pencil(Stationery):
    def meth_draw(self, title='pencil'):
        print(f"“Запуск отрисовки. ”{title}")

    pass

class Handle(Stationery):
    def meth_draw(self, title='handle'):
        print(f"“Запуск отрисовки. ”{title}")
    pass


fir_o = Pen()
sec_o = Pencil()
th_o = Handle()

print(fir_o.meth_draw())
print(sec_o.meth_draw())
print(th_o.meth_draw())
