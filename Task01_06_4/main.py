"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
color, name, i s_police ( булево). А также методы: go, stop, t urn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
show_speed, который должен показывать текущую скорость автомобиля. Для классов
TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
( TownCar ) и 40 ( WorkCar ) должно выводиться сообщение о превышении скорости."""

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
        print(f"Новая машина марки {self.name}, ее цвет {color}. Это полицейская машина {self.is_police}?")

    def go(self):
        print(f"Машина {self.name} поехала.")

    def stop(self):
        print(f"Машина {self.name} остановилась.")

    def turn(self, direction):
        print(f"Машина {self.name} повернула {'налево' if direction==0 else 'направо'}.")

    def showSpeed(self):
        print(f"Машина {self.name} двигается со скоростью {self.speed}.")


class TownCar(Car):
    def showSpeed(self):
        if self.speed>60:
            print(f"{self.name}: превышение скорости! Текущая скорость {self.speed}")
        else:
            print(f"{self.name} двигается со скоростью {self.speed}.")

class WorkCar(Car):
    def showSpeed(self):
        if self.speed>40:
            print(f"{self.name}: превышение скорости! Текущая скорость {self.speed}")
        else:
            print(f"{self.name} двигается со скоростью {self.speed}.")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


policeCar = PoliceCar(80,"white", "полиция")
print(policeCar.go())
print(policeCar.showSpeed())
print(policeCar.turn(1))
print(policeCar.turn(0))
print(policeCar.stop())

workCar = WorkCar(80,"white", "грузовичок")
print(workCar.go())
print(workCar.showSpeed())
print(workCar.turn(1))
print(workCar.turn(0))
print(workCar.stop())