class Groups:
    amount = 0

    def __init__(self, name_group):
        self.name_group = name_group

    def print_inf(self):
        print(f"Группа: {self.name_group}, количевство студентов: {self.amount}")