from field import Field
from field_object import Field_object
from position import Position
from game_status import Game_status

# To handle keyboard presses
import getch

import config

class Game:
    def __init__(self):
        self.game_status = Game_status.RUN
        self.field = Field(config.WIDTH, config.HEIGHT)
        self.field_object = Field_object(Position(config.START_POSITION[0], config.START_POSITION[1]), config.DEFAULT_PLAYER_BODY)

    def controls(self, move):
        if move in ['a', 'd', 'w', 's']: # Should rewrire to match-case variant
            if move == "a":
                self.field_object.position.move_left()
            if move == "d":
                self.field_object.position.move_right()
            if move == "w":
                self.field_object.position.move_up()
            if move == "s":
                self.field_object.position.move_down()
        else:
            print("Wrong input")
    
    def collision(self):
        if self.field_object.position.pos_x < 1:
            self.game_status = Game_status.OVER
        if self.field_object.position.pos_x > config.WIDTH - 2:
            self.game_status = Game_status.OVER
        if self.field_object.position.pos_y < 1:
            self.game_status = Game_status.OVER
        if self.field_object.position.pos_y > config.HEIGHT - 2:
            self.game_status = Game_status.OVER

    def run(self):
        while self.game_status == Game_status.RUN:
            self.field.init()
            self.field.add_object(self.field_object)
            self.field.render()
            print(self.field_object.position)
            move = getch.getch()
            self.controls(move)
            self.collision()
        print("Game is over")
