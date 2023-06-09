from dataclasses import dataclass

class Movable:
    def move_up(self):
        ...
    
    def move_down(self):
        ...

    def move_left(self):
        ...

    def move_right(self):
        ...

@dataclass
class Position(Movable):
    pos_x: int
    pos_y: int

    def move_up(self):
        self.pos_y -= 1
    
    def move_down(self):
        self.pos_y += 1

    def move_left(self):
        self.pos_x -= 1

    def move_right(self):
        self.pos_x += 1