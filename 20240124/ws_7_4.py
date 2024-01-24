# 아래 클래스를 수정하시오.
class Shape:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_info(self):
        print("width:" + str(self.width))
        print("height:" + str(self.height))
        print("Area:" + str(self.width * self.height))
        print("Perimeter:" + str(self.width * 2 + self.height * 2))


shape1 = Shape(5, 3)
shape1.print_info()
