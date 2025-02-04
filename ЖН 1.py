import math
class Figure():
    sides_count = 0

    def __init__(self, color: tuple, *sides: int, filled: bool = True):
        if len(sides) != self.sides_count:
            self.__sides = [self.sides_count]
        else:
            self.__sides = list(sides)
        self.__color = color
        self.filled = filled

    def get_color(self):
        return list(self.__color)


    def __is_valid_color(self, r, g, b):
        lst = [r, g, b]
        lst.sort()
        if lst[0] < 0 or lst[-1] > 255:
            return False
        else:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, sides):
        res = []
        for i in sides:
            if i > 0:
                res.append(i)
        if len(res) > 0 and len(sides) == len(self.__sides):
            return True
        else:
            return False

    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = sides

    def get_sides(self):
        return [*self.__sides]

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):

    sides_count = 1

    def __radius(self):
        return self.__len__ * (2/3.14)

    def get_square(self):
        return (self.__len__**2)/(4*3.14)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = 1/2 * (self.get_sides()[0] + self.get_sides()[1] + self.get_sides()[2])
        s = math.sqrt(p * ((p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])))
        return s



class Cube(Figure):
    sides_count = 12

    def __init__(self, color,  *sides: int, filled: bool = True):
        super().__init__(color, *sides, filled)
        if len(sides) == 1:
            for i in sides:
                self.__sides = self.sides_count*[i]
        else:
            self.__sides = self.sides_count

    def get_sides(self):
        return [*self.__sides]

    def get_volume(self):
        return self.__sides[1]**3



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), )



