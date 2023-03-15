import os


class File:
    def __init__(self):
        self._path = ""
        self._expansions = [".txt", ".csv"]
        self._exist = False
        self._isOpen = False

    def get_expansion(self, name):
        for expansion in self._expansions:
            if expansion in name:
                return expansion

    def get_path(self):
        return self._path

    def set_path(self, path):
        self._path = path

    def is_exist(self, fpath, name):
        if os.path.exists(fpath + f"/{name}"):
            self._exist = True
            self._path = fpath + f"/{name}"
            return True
        return False

    def open_file(self):
        self._isOpen = True

    def is_open(self):
        return self._isOpen

    def right_exp(self, name):
        for expansion in self._expansions:
            if expansion in name:
                return True
        return False

    def get_exp(self, file_name):
        for expansion in self._expansions:
            if expansion in file_name:
                return expansion

    def create_file(self, fpath, name):
        if self.right_exp(name):
            self._path = f"{fpath}/{name}"
            f = open(self._path, 'w+')
            print("Файл создан")
            f.close()

