"""Реализовать базовый класс Worker ( работник), в котором определить атрибуты: name,
surname, position ( должность), income ( доход). Последний атрибут должен быть
защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position ( должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника ( get_full_name) и
дохода с учетом премии ( get_total_income) . Проверить работу примера на реальных данных
(создать экземпляры класса Position , передать данные, проверить значения атрибутов,
вызвать методы экземпляров)."""

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit" : wage, "bonus" : bonus}

class Position(Worker):
    def getFullName(self):
        return f"{self.name} {self.surname}"

    def getFullProfit(self):
        return f"{sum(self._income.values())}"


manager = Position("Dorian", "Gray", "CEO", 50000, 12500)
print(manager.getFullProfit())
print(manager.getFullName())
print(manager.position)