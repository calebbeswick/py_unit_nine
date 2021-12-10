class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def perimiter(self):
        return (self.width * 2) + (self.length * 2)

    def area(self):
        return self.width * self.length