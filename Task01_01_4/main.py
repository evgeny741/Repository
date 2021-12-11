"""Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции."""

inputCount = input("Введите длинное положительное число: ")
lenCount = len(inputCount)
result = 0

while lenCount>0:
    temp = int(inputCount) % 10
    if result < temp:
        result = temp
    inputCount=int(inputCount)//10
    lenCount-=1

print("Максимальное число ", result)