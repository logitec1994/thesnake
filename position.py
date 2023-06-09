class Movable:
    def move_up(self):
        ...
    
    def move_down(self):
        ...

    def move_left(self):
        ...

    def move_right(self):
        ...

class Position(Movable):
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def move_up(self):
        self.pos_x -= 1
    
    def move_down(self):
        self.pos_x += 1

    def move_left(self):
        self.pos_y -= 1

    def move_right(self):
        self.pos_y += 1