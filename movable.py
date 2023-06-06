from abc import ABC

class Movable(ABC):
    def move_up(self):
        ...
    
    def move_down(self):
        ...

    def move_left(self):
        ...

    def move_right(self):
        ...
