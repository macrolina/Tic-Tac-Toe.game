from random import choice
from .bot_main import Bot

class BotMediumMode(Bot):
    def __init__(self, figure, board, use_figure, group, choose, event):
        super().__init__(figure, board, use_figure, group, choose, event)

    def bot_move(self):
        bot = self.bot_choose()
        bot_think = self.bot_think_move()

        if bot_think != None and self.board[bot_think[0]][bot_think[1]]==None:
            try:
                self.use_figure.rect.x = self.choose[bot_think[0]][bot_think[1]][0]
                self.use_figure.rect.y = self.choose[bot_think[0]][bot_think[1]][1]

                self.choose[bot_think[0]][bot_think[1]] = None
                self.board[bot_think[0]][bot_think[1]] = "O"

                self.group.add(self.use_figure)
            except Exception:
                print("error")

        elif bot != None:

            index = []

            for i in range(len(self.choose)):

                if index != []:
                    break

                try:

                    index = [i, self.choose[i].index(bot)]

                except:

                    pass

            if self.figure == "circle":

                self.use_figure.rect.x = bot[0]

                self.use_figure.rect.y = bot[1]

                self.choose[index[0]][index[1]] = None

                self.board[index[0]][index[1]] = "O"

                self.group.add(self.use_figure)

    def bot_think_move(self):
        for number, row in enumerate(self.board):
            if row[0] == row[1]!=None and row[2] == None:
                return [number, 2]
            elif row[1] == row[2]!=None and row[0] == None:
                return [number, 0]
            elif row[0] == row[2]!=None and row[1] == None:
                return [number, 1]

        for i in range(3):
            if self.board[0][i] == self.board[1][i]!=None and self.board[2][i] == None:
                return [2, i]
            elif self.board[1][i] == self.board[2][i]!=None and self.board[0][i] == None:
                return [0, i]
            if self.board[0][i] == self.board[2][i]!=None and self.board[1][i] == None:
                return [1, i]

        if self.board[0][0] == self.board[1][1]!=None and self.board[2][2] == None:
            return [2, 2]
        elif self.board[1][1] == self.board[2][2]!=None and self.board[0][0] == None:
            return [0, 0]
        elif self.board[0][0] == self.board[2][2]!=None and self.board[1][1] == None:
            return [1, 1]

        if self.board[0][2] == self.board[1][1]!=None and self.board[2][0] == None:
            return [2, 0]
        elif self.board[1][1] == self.board[2][0]!=None and self.board[0][2] == None:
            return [2, 0]
        elif self.board[0][2] == self.board[2][0]!=None and self.board[1][1] == None:
            return [1, 1]