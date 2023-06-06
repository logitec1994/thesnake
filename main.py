import time

import getch

from field import Field
from size import Size
from field_object import Field_object
from coordinate import Coordinate
from point import Point

if __name__ == "__main__":
    game_condition = True
    rows = 15
    cols = 45
    s = Size(width=cols, height=rows)
    f = Field(s)
    p = Point(2, 2)
    c = Coordinate(p)
    fo = Field_object("T", c)
    f.add(fo)
    while game_condition:
        f.render()
        if not f.collision():
            move = getch.getch()
            match move:
                case 'a': f.field_objects[0].move_left()
                case 'd': f.field_objects[0].move_right()
                case 's': f.field_objects[0].move_down()
                case 'w': f.field_objects[0].move_up()
        else:
            print("Game is over")
            break    
        time.sleep(0.1)
