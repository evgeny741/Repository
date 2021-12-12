"""Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
сохранить на своем месте. Для заполнения списка элементов необходимо использовать
функцию input() ."""

myList = []
result = 0

while True:
    stopPhrase = input("Введите значение")
    if stopPhrase == "stop":
        break
    else:
        myList.append(stopPhrase)

lenList = len(myList)
if lenList % 2 == 1:
    lenList -= 1

while result < lenList & lenList >= 2:
    temp = myList[result]
    myList[result] = myList[result + 1]
    myList[result + 1] = temp
    result += 2

print(myList)
