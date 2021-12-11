"""Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
ввёл число 3. Считаем 3 + 33 + 333 = 369."""

userCount = input("Введите число от 1 до 9: ")
print(f"{userCount} + {userCount*2} + {userCount*3} = {int(userCount)+ int(userCount*2) + int(userCount*3)}")