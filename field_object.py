from dataclasses import dataclass
from movable import Movable
from coordinate import Coordinate
from point import Point

@dataclass
class Field_object(Movable):
    content: chr
    coordinate: Coordinate

    def move_down(self):
        self.coordinate.get_coordinate().x += 1
    
    def move_up(self):
        self.coordinate.get_coordinate().x -= 1

    def move_left(self):
        self.coordinate.get_coordinate().y -= 1

    def move_right(self):
        self.coordinate.get_coordinate().y += 1
