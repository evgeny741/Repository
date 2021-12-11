"""Поработайте с переменными, создайте несколько, выведите на экран, запросите у
пользователя несколько чисел и строк и сохраните в переменные, выведите на экран."""

import datetime

hello = "Hello world!"
count = 123123123

print(hello)
print(count)

myName = input("Введите Ваше имя: ")
myDateBirth = int(input("Введите число Вашего дня рождения: "))
today = int(datetime.date.today().day)

print(f"Уважаемый {myName}, до Вашего дня рождения осталось {abs(today-myDateBirth)}")




