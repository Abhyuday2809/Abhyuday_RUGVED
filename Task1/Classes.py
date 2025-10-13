from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, c):
        self.color = c

    def get_color(self):
        return self.color

    @abstractmethod
    def get_area(self) -> float:
        pass

class Square(Shape):
    def __init__(self, c, side):
        super().__init__(c)
        self.side = side

    def get_area(self) -> float:
        return self.side * self.side

if __name__ == "__main__":
    my_square = Square("Red", 5.5)

    print(f"The color of the square is: {my_square.get_color()}")

    area = my_square.get_area()
    print(f"The side of the square is: {my_square.side}")
    print(f"The area of the square is: {area}")

    blue_square = Square("Blue", 10)
    print(f"\nCreated another square.")
    print(f"Color: {blue_square.get_color()}")
    print(f"Area: {blue_square.get_area()}")

