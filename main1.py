import os
import sys
def add_new_user(name: str, phone: str, filename: str):
    """
    Добавление нового пользователя.
    """
    new_line = '\n' if read_all(filename) != "" else ''
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{new_line}{name} - {phone}")


def read_all(filename: str) -> str:
    """
    Возвращает все содержимое телефонной книги.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def search_user(filename: str, data: str) -> str:
    """
    Поиск записи по критерию data.
    """
    with open(filename, "r", encoding="utf-8") as file:
        list_1 = file.read().split("\n")
    result = []
    result = [i for i in list_1 if data in i]
    if not result:
        return "По указанному значению совпадений не найдено"
    return "\n".join(result)
def transfer_data(source, dest, num_row):
    # Считываем все строки из исходного файла
    with open(source, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    if num_row < 1 or num_row > len(lines):
        return "Неверный номер строки"
    
    # Получаем строку для переноса
    line_to_transfer = lines.pop(num_row - 1)  # Удаляем строку из списка
    
    # Добавляем строку в целевой файл
    with open(dest, "a", encoding="utf-8") as file:
        file.write("\n" + line_to_transfer.strip())  # Добавляем в новый файл
    
    # Обновляем исходный файл после удаления строки
    with open(source, "w", encoding="utf-8") as file:
        file.writelines(lines)
INFO_STRING = """
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - перенос записи в другой файл
"""

file_source = "Text.txt"
file_dest = "Dest.txt"

# Проверка наличия исходного файла
if file_source not in os.listdir():
    print("Исходный файл отсутствует")
    sys.exit()

while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(file_source))
    elif mode == 2:
        name = input("Введите Ваше имя: ")
        phone = input("Введите Ваш телефон: ")
        add_new_user(name, phone, file_source)
    elif mode == 3:
        data = input("Введите значение для поиска: ")
        print(search_user(file_source, data))
    elif mode == 4:
        row_number = int(input("Введите номер строки для переноса: "))
        result = transfer_data(file_source, file_dest, row_number)
        print(result)
