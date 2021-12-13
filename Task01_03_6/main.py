"""Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) ->
Text."""


def int_func(userString):
    return userString.capitalize()
#Ну или userString.title() - все слова будут с заглавной


userString = "sadc"

print("Первоначальная строка:", userString)
print("Строка после функции:", int_func(userString))
