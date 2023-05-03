class Rectangle:
    def __init__(self, width, height):
        # initialize width and height attributes
        self.width = width
        self.height = height

    def area(self):
        # calculate and return the area of the rectangle
        return self.width * self.height

    def perimeter(self):
        # calculate and return the perimeter of the rectangle
        return 2 * (self.width + self.height)