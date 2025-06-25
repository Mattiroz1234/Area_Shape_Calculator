from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def __str__(self):
        area_str = f"{self.get_area():.2f}"
        try:
            perimeter_str = f"{self.get_perimeter():.2f}"
        except ValueError:
            perimeter_str = self.get_perimeter()
        return f"{self.name} | Area: {area_str} | Perimeter: {perimeter_str}"

