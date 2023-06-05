import time

from field import Field
from size import Size


if __name__ == "__main__":
    game_condition = True
    rows = 15
    cols = 45
    s = Size(width=cols, height=rows)
    f = Field(s)
    while game_condition:
        f.render()
        time.sleep(0.4)
