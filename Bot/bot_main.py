from random import choice
from Event_check import Game

class Bot:
    def __init__(self, figure: str, board, use_figure, group, choose, event):
        self.figure = figure
        self.board = board
        self.use_figure = use_figure
        self.group = group
        self.choose=choose
        self.event=event
    def bot_choose(self) -> list[int, int]:
        if [y for y in self.choose if y != [None, None, None]] != []:
            row = choice([y for y in self.choose if y != [None, None, None]])
            bot = choice([x for x in row if x != None])
            return bot
        else:
            if Game(self.board, self.event)==None:
                return self.event.equally()

    def bot_move(self):
        pass