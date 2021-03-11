class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()


class SquareImageArea(ImageArea):
    def __init__(self, side):
        super().__init__(side, side)


a1 = SquareImageArea(7)  # 70
a2 = SquareImageArea(7)  # 70
a3 = SquareImageArea(8)  # 72
print(a1 == a2)  # True
print(a1 != a3)  # True
print(a1 != a2)  # False
print(a1 >= a3)  # False
print(a1 <= a2)  # True
print(a1 < a3)  # True
