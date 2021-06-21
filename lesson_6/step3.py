class Worker:

    def __init__(self, name, surname, position, __income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = __income


class Position(Worker):

    def __init__(self, name, surname, position, __income):
        super().__init__(name, surname, position, __income)

    def get_full_name(self):
        print(f"Name: {self.name}\nSurname: {self.surname}")

    def get_total_income(self):
        pass
        # print(f"Income {self.__}")


p = Position("Anton", "Ivanov", "Manager", 2000)
p.get_full_name()
