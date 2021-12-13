"""Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Реализовать вывод данных о
пользователе одной строкой."""


def userDefine(*kwargs):
    return f"{name} {family} {years} {city} {email} {phone}"


name = "Evgeny"
family = "Markin"
years = 1978
city = "Magnitogorsk"
email = "1@1.ru"
phone = "+7(904)123-45-67"

print(userDefine(name, family, years, city, phone, email))
