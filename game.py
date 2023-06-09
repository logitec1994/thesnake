from field import Field
from field_object import Field_object
from position import Position
from game_status import Game_status


class Game:
    def __init__(self):
        self.game_status = Game_status.OVER

    def controls(self):
        ...
    
    def collision(self):
        ...

    def run(self):
        width = 13
        height = 13
        p = Position(x=2, y=1)
        f = Field(width, height)
        fo = Field_object(p, "T")
        f.init()
        f.add_object(fo)
        f.render()
        fo.position.move_left()
        f.add_object(fo)
        f.render()
        print(fo.position)