import csv

import pandas as pd
from tabulate import tabulate

import file


class CsvFile(file.File):
    data = []
    keys = []

    def get_data(self):
        self.data, keys = [], []
        with open(self.get_path(), "r", encoding="cp1251") as f:
            reader = csv.DictReader(f)
            self.keys = reader.fieldnames
            for row in reader:
                self.data.append(row)
            f.close()

    def set_data(self, data, keys):
        with open(self.get_path(), "w", encoding="cp1251", newline="\n") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
            f.close()

    @staticmethod
    def add_new_data(data, keys):
        n = int(input("Кол-во строк: "))
        for v in range(len(data), len(data) + n):
            print("Введите строку в соответствии с ключами через запятую:")
            for key in keys:
                print(key, end=" ")
            print()

            input_row = input().split(",")

            if len(input_row) == len(keys):
                new_row = {}
                for i in range(len(keys)):
                    new_row[keys[i]] = input_row[i]
                data.append(new_row)
            else:
                print("Ошибка!")

    @staticmethod
    def print_data(data, keys):
        print("Данные из файла:")
        flag = True
        while flag:
            if len(data) != 0:
                print(tabulate(pd.DataFrame(data), headers=keys, tablefmt='grid', showindex=False))
                flag = False
            else:
                print("Пустой файл")

    def write_keys(self):
        key = []
        print("Введите ключи через запятую")
        key = input().split(",")
        if len(key) == 0:
            print("Вы ничего не ввели!")
        self.keys = key


