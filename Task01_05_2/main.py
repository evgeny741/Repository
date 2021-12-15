"""Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке."""

with open("text1.txt", "r", encoding="utf-8") as f:
    myLine = f.readlines()
    for index, value in enumerate(myLine, 1):
        numWord = len(value.split())
        print(f"Строка {index} содержит {numWord} слов")