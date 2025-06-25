from calculator import Shape

class Square(Shape):
    def __init__(self, side):
        super().__init__(name="Square")
        if side <= 0 :
            raise ValueError("side must be positive number.")
        self.side = side

    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return self.side * 4