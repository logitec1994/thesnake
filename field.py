from os import system
from dataclasses import dataclass, field
from size import Size
from field_object import Field_object

@dataclass
class Field:
    size: Size
    field_objects: list[Field_object] = field(default_factory=list)    

    def __generate(self):
        self.matrix = [[" "] * self.size.width for _ in range(self.size.height)]

    def __fill(self):
        for i in range(self.size.width):
            self.matrix[0][i] = "#"
            self.matrix[self.size.height - 1][i] = "#"
        
        for i in range(1, self.size.height - 1):
            self.matrix[i][0] = "#"
            self.matrix[i][self.size.width - 1] = "#"

    def add(self, obj: Field_object):
        self.field_objects.append(obj)

    def __add_object(self):
        for i, v in enumerate(self.field_objects):
            self.matrix[self.field_objects[i].position.x][self.field_objects[i].position.y] = self.field_objects[i].content

    def render(self):
        system("clear")
        self.__generate()
        self.__fill()
        self.__add_object()
        for row in self.matrix:
            print(" ".join(str(element) for element in row))
