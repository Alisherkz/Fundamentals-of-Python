class Road:

    def __init__(self, __lenght, __width):
        self.__lenght = __lenght
        self.__width = __width

    def res(self):
        result = self.__lenght * self.__width * 25 * 5
        return result / 1000

ro = Road(20, 5000)
print(ro.res())