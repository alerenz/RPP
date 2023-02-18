class Students():
    count = 0
    def __init__(self, surname,name,group):
        self.name = name
        self.surname = surname
        self.group = group
    def print_inf(self):
        print(f"{self.surname} {self.name} {self.group}")