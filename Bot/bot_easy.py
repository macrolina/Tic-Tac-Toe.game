from random import choice
from .bot_main import Bot

class BotEasyMode(Bot):
    def __init__(self, figure, board, use_figure, group, choose, event):
        super().__init__(figure, board, use_figure, group, choose, event)

    def bot_move(self):
        bot=super().bot_choose()
        index = []
        for i in range(len(self.choose)):
            if index != []:
                break
            try:
                index = [i, self.choose[i].index(bot)]
            except:
                pass

        if self.figure=="circle":
            self.use_figure.rect.x = bot[0]
            self.use_figure.rect.y = bot[1]

            self.choose[index[0]][index[1]] = None
            self.board[index[0]][index[1]] = "O"

            self.group.add(self.use_figure)
