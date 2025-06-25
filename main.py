from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle
from hexagon import Hexagon

def print_menu():
    print("\n Area Shape Resolver Calculator")
    print("1. Rectangle")
    print("2. Square")
    print("3. Triangle")
    print("4. Circle")
    print("5. Hexagon")
    print("0. Exit")


def get_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            return val
        except ValueError:
            print("Invalid input, Please enter a number.")

def main():
    while True:
        print_menu()
        choice = input("Select a shape (0-5): ")

        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "1":
            width = get_float("Enter width: ")
            height = get_float("Enter height: ")
            shape = Rectangle(width, height)

        elif choice == "2":
            side = get_float("Enter side length: ")
            shape = Square(side)

        elif choice == "3":
            base = get_float("Enter base: ")
            height = get_float("Enter height: ")
            shape = Triangle(base, height)

        elif choice == "4":
            radius = get_float("Enter radius: ")
            shape = Circle(radius)

        elif choice == "5":
            side = get_float("Enter side length: ")
            shape = Hexagon(side)

        else:
            print("Invalid choice, Please select from 0–5.")
            continue

        print("\n Shape Details:")
        print(shape)


def create_shapes():
    shapes = [
        Rectangle(4, 6),
        Square(5),
        Triangle(3, 4),
        Circle(7),
        Hexagon(2)
    ]

    for shape in shapes:
        print(shape)



if __name__ == "__main__":
    #main()
    create_shapes()
