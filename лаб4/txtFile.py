import file


class TxtFile(file.File):
    data = []

    def get_data(self):
        with open(self.get_path(), "r",encoding="utf-8") as f:
            for line in f:
                self.data.append(line)
            f.close()

    def set_data(self, data):
        with open(self.get_path(), "w") as f:
            f.writelines("%s\n" % row for row in data)
            f.close()

    def print_data(self):
        print("Данные из файла:")
        s = ""
        for row in self.data:
            if row.__contains__("\n"):
                print(f"{s:>2}{row}", end='')
            else:
                print(f"{s:>2}{row}")
        print()

    @staticmethod
    def add_new_data_to_txt_file(data):
        print("в конце введите ....(4 точки)")
        flag = True
        while flag:
            s = input()
            if s == "....":
                flag = False
            else:
                data.append(s)



