from enum import Enum, auto

class Status(Enum):
    RUN = auto()
    OVER = auto()

class Game:
    def __init__(self):
        self.game_status = Status.OVER
        self.field = 0
        self.player = 0

    def controls(self):
        ...
    
    def collision(self):
        ...

    def run(self):
        width = 0
        height = 0

if __name__ == "__main__":
    game = Game()
    game.run()