from dataclasses import dataclass
from point import Point

@dataclass
class Coordinate:
    __coordinates: Point

    def get_coordinate(self):
        return self.__coordinates
