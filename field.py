from os import system

from field_object import Field_object

class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __generate(self):
        self.matrix = [[" "] * self.width for _ in range(self.height)]
        return self.matrix

    def __fill(self):
        for i in range(self.width):
            self.matrix[0][i] = "#"
            self.matrix[self.height - 1][i] = "#"
        
        for i in range(1, self.height - 1):
            self.matrix[i][0] = "#"
            self.matrix[i][self.width - 1] = "#"

    def init(self):
        self.__generate()
        self.__fill()
    
    def add_object(self, obj: Field_object):
        self.matrix[obj.position.pos_y][obj.position.pos_x] = obj.body

    def render(self):
        system("clear")
        for row in self.matrix:
            print(" ".join(str(element) for element in row))
