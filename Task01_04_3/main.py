"""Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить
задание в одну строку."""

uniqCount = [element for element in range(20, 240) if element % 20 == 0 or element % 21 == 0]
print(uniqCount)
