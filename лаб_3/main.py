import operator
import os
import csv
import datetime
from tabulate import tabulate
import pandas as pd


def add_new_data(data, keys):
    n = int(input("Кол-во строк: "))
    print("Введите только ФИО и Тип обращения через запятую")
    for i in range(len(data), len(data) + n):
        row = input().split(",")
        new_row = {
            keys[0]: str(len(data) + 1),
            keys[1]: row[0],
            keys[2]: str(datetime.datetime.now()),
            keys[3]: row[1],
        }
        data.append(new_row)


def write_file(data, keys, file):
    data.sort(key=operator.itemgetter(keys[0]))
    with open(file, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
        file.close()


def action_data(sort_i, data, keys, file):
    if sort_i == 1:
        return data.sort(key=operator.itemgetter(keys[1]))
    if sort_i == 2:
        return data.sort(key=operator.itemgetter(keys[0]))
    if sort_i == 3:
        return data.sort(key=operator.itemgetter(keys[2]))
    if sort_i == 4:
        add_new_data(data, keys)
        write_file(data, keys, file)
    if sort_i == 0:
        return data


def print_data(data, keys):
    flag = True
    while flag:
        if len(data) != 0:
            print(tabulate(pd.DataFrame(data), headers=keys, tablefmt='grid', showindex=False))
            flag = False
        else:
            print("Пустой файл")


def get_data(file):
    data, keys = [], []
    with open(file, "r") as file:
        reader = csv.DictReader(file)
        keys = reader.fieldnames
        for row in reader:
            data.append(row)
        file.close()

    return data, keys


def file_set(path):
    file_name = input("Введите название файла: ")
    file = f"{path}/{file_name}"
    if os.path.exists(file):
        print("файл найден")
        return file
    else:
        print("Ошибка: такой файл не существует.\n"
              "1 - попробовать ещё раз\n"
              "0 - выход")
        op = int(input("введите команду: "))
        if op == 1:
            file = file_set(path)
            return file
        if op == 0:
            return


def read_file():
    with open('data.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            print(row)


def print_information(arr):
    print(f"Всего файлов: {len(arr)}")
    k = 1
    for i in arr:
        print(f"{k}: {i}")
        k += 1


def director():
    path = input("Введите путь и папку:")
    if os.path.exists(path):
        print("папка найдена")
        return path
    else:
        print("Ошибка: такой папки не существует.\n"
              "1 - попробовать ещё раз\n"
              "0 - выход")
        op = int(input("введите команду: "))
        if op == 1:
            director()
        if op == 0:
            return


def print_file(path):
    flag = True
    while flag:
        if os.path.exists(path):
            print_information(os.listdir(path))
            return
        else:
            print("папки по этому пути не существует.\n"
                  "1 - попробовать ещё раз \n"
                  "0  -выход \n")
            op = int(input("введите команду: "))
            if op == 0:
                flag = False
            if op == 1:
                path = print_file(path)
                return path
            if op > 1:
                print("введите 1 или 0")


def main():
    path = ''
    file = ''
    data = []
    keys = []
    while True:
        print(f"1 - вывод файлов в директории\n"
              f"2 - вывод данных из файла .csv\n"
              f"0 - выход\n")
        itype = int(input())
        if itype == 1:
            path = director()
            print_file(path)
        if itype == 2:
            now = True
            called1 = False
            called2 = False
            while now:
                if path == '' or path is None:
                    if not called1:
                        path = director()
                        called1 = True
                    else:
                        now = False
                else:
                    if file == '' or file is None:
                        if not called2:
                            file = file_set(path)
                            called2 = True
                        else:
                            now = False
                    else:
                        if len(data) == 0:
                            data, keys = get_data(file)
                        else:
                            print_data(data, keys)
                            print(f"Выберите вид сортировки или добавить данные:\n"
                                  f"1 - По ФИО\n"
                                  f"2 - По номеру\n"
                                  f"3 - По дате и времени\n"
                                  f"4 - Добавить данные\n"
                                  f"0 - Выход\n")
                            sort_i = int(input())
                            action_data(sort_i, data, keys, file)
                            print_data(data, keys)
                            now = False
        if itype == 0:
            exit(1)


if __name__ == '__main__':
    main()


