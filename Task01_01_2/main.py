"""Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
выведите в формате чч:мм:сс. Используйте форматирование строк."""

userTime = int(input("Введите время в секундах: "))

userHour = userTime//3600
userMinutes = (userTime%3600)//60
userSecunda = (userTime%3600)%60

print(f"{userHour:02} часов {userMinutes:02} минут {userSecunda:02} секунд")