"""Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict."""

yearSeason = {"зима": [1, 2, 12], "весна": [3, 4, 5], "лето": [6, 7, 8], "осень": [9, 10, 11]}

userInput = int(input("Введите номер месяца от 1 до 12: "))

if 0 < userInput <= 12:
    for key, value in yearSeason.items():
        if userInput in value:
            print("Сейчас", key)
            break
        else:
            continue
else:
    print("Вы ввели неверное значение!")
