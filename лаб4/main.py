import os

import csvFile
import txtFile


@staticmethod
def director(path):
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


@staticmethod
def file_set(path, file_name):
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
            file = file_set(path, file_name)
            return file
        if op == 0:
            return


def main():
    print("Работа с файлами:\n"
          "С каким файлом хотите работать?\n"
          "1 - csv файл\n"
          "2 - txt файл\n"
          "0 - выход")
    oper = int(input("Введите команду:"))
    match(oper):
        case 1:
            print("Выберите действие:\n"
                  "1 - Открыть существующий файл\n"
                  "2 - Создать новый\n"
                  "0 - выход")
            oper = int(input("Введите команду:"))
            match(oper):
                case 1:
                    file1 = csvFile.CsvFile()
                    path = input("Введите путь:")
                    file_name = input("Введите название файла:")
                    full_path = file_set(path, file_name)
                    file1.set_path(full_path)
                    file1.get_data()
                    file1.print_data(file1.data, file1.keys)
                    print("Хотите ввести новые данные в файл?\n"
                          "1 - Да\n"
                          "2 - Нет, выход")
                    oper = int(input("Введите команду:"))
                    match(oper):
                        case 1:
                            file1.add_new_data(file1.data, file1.keys)
                            file1.set_data(file1.data, file1.keys)
                            file1.print_data(file1.data, file1.keys)

                        case 2:
                            exit(1)
                case 2:
                    file2 = csvFile.CsvFile()
                    path = input("Введите путь:")
                    file_name = input("Введите название файла:")
                    file2.create_file(path, file_name)
                    print("Хотите ввести новые данные в файл?\n"
                          "1 - Да\n"
                          "2 - Нет, выход")
                    oper = int(input("Введите команду:"))
                    match (oper):
                        case 1:
                            file2.write_keys()
                            file2.add_new_data(file2.data, file2.keys)
                            file2.set_data(file2.data, file2.keys)
                            file2.print_data(file2.data, file2.keys)

                        case 2:
                            exit(1)
                case 0:
                    exit(1)
        case 2:
            print("Выберите действие:\n"
                  "1 - Открыть существующий файл\n"
                  "2 - Создать новый\n"
                  "0 - выход")
            oper = int(input("Введите команду:"))
            match (oper):
                case 1:
                    file_txt = txtFile.TxtFile()
                    path1 = input("Введите путь:")
                    file_name1 = input("Введите название файла:")
                    full_path1 = file_set(path1, file_name1)
                    file_txt.set_path(full_path1)
                    file_txt.get_data()
                    file_txt.print_data()
                case 2:
                    file_txt2 = txtFile.TxtFile()
                    path1 = input("Введите путь:")
                    file_name1 = input("Введите название файла:")
                    file_txt2.create_file(path1, file_name1)
                    print("Хотите ввести новые данные в файл?\n"
                          "1 - Да\n"
                          "2 - Нет, выход")
                    oper = int(input("Введите команду:"))
                    match (oper):
                        case 1:
                            file_txt2.add_new_data_to_txt_file(file_txt2.data)
                            file_txt2.set_data(file_txt2.data)
                            file_txt2.print_data()
                        case 2:
                            exit(1)
                case 0:
                    exit(1)


if __name__ == '__main__':
    main()
