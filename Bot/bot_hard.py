from random import choice
from .bot_main import Bot

class BotHardMode(Bot):
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
                pass


        elif bot != None:
            index = []
            for i in range(len(self.choose)):
                if index != []:
                    break
                try:
                    index = [i, self.choose[i].index(bot)]
                except:
                    pass

                print("Second if works")

            if self.figure == "circle":
                self.use_figure.rect.x = bot[0]
                self.use_figure.rect.y = bot[1]

                print("Circle works")

                self.choose[index[0]][index[1]] = None
                self.board[index[0]][index[1]] = "O"

                self.group.add(self.use_figure)

    def bot_think_move(self) -> list[int]|None:
        for number, row in enumerate(self.board):
            if row[0] == row[1] == "O" and row[2] == None:
                return [number, 2]
            elif row[1] == row[2] == "O" and row[0] == None:
                return [number, 0]
            elif row[0] == row[2] == "O" and row[1] == None:
                return [number, 1]

        for i in range(3):
            if self.board[0][i] == self.board[1][i] == "O" and self.board[2][i] == None:
                return [2, i]
            elif self.board[1][i] == self.board[2][i] == "O" and self.board[0][i] == None:
                return [0, i]
            if self.board[0][i] == self.board[2][i] == "O" and self.board[1][i] == None:
                return [1, i]

        if self.board[0][0] == self.board[1][1] == "O" and self.board[2][2] == None:
            return [2, 2]
        elif self.board[1][1] == self.board[2][2] == "O" and self.board[0][0] == None:
            return [0, 0]
        elif self.board[0][0] == self.board[2][2] == "O" and self.board[1][1] == None:
            return [1, 1]

        if self.board[0][2] == self.board[1][1] == "O" and self.board[2][0] == None:
            return [2, 0]
        elif self.board[1][1] == self.board[2][0] == "O" and self.board[0][2] == None:
            return [2, 0]
        elif self.board[0][2] == self.board[2][0] == "O" and self.board[1][1] == None:
            return [1, 1]

        for number, row in enumerate(self.board):
            if row[0] == row[1] == "X" and row[2] == None:
                return [number, 2]
            elif row[1] == row[2] == "X" and row[0] == None:
                return [number, 0]
            elif row[0] == row[2] == "X" and row[1] == None:
                return [number, 1]

        for i in range(3):
            if self.board[0][i] == self.board[1][i] == "X" and self.board[2][i] == None:
                return [2, i]
            elif self.board[1][i] == self.board[2][i] == "X" and self.board[0][i] == None:
                return [0, i]
            if self.board[0][i] == self.board[2][i] == "X" and self.board[1][i] == None:
                return [1, i]

        if self.board[0][0] == self.board[1][1] == "X" and self.board[2][2] == None:
            return [2, 2]
        elif self.board[1][1] == self.board[2][2] == "X" and self.board[0][0] == None:
            return [0, 0]
        elif self.board[0][0] == self.board[2][2] == "X" and self.board[1][1] == None:
            return [1, 1]

        if self.board[0][2] == self.board[1][1] == "X" and self.board[2][0] == None:
            return [2, 0]
        elif self.board[1][1] == self.board[2][0] == "X" and self.board[0][2] == None:
            return [2, 0]
        elif self.board[0][2] == self.board[2][0] == "X" and self.board[1][1] == None:
            return [1, 1]

        if self.board[0][0] == self.board[1][1] == "X" and self.board[2][2] == "O":
            return choice([[0, 2], [0, 2]])
        elif self.board[1][1] == self.board[2][2] == "X" and self.board[0][0] == "O":
            return choice([[0, 2], [0, 2]])

        if self.board[0][2] == self.board[1][1] == "X" and self.board[2][0] == "O":
            return choice([[0, 0], [2, 2]])
        elif self.board[1][1] == self.board[2][0] == "X" and self.board[0][2] == "O":
            return choice([[0, 0], [2, 2]])

        if self.board[0].count(None) == 3 and self.board[1].count(None) == 2 and self.board[2].count(None) == 3 and self.board[1][1] == "X":
            return choice([[0, 0], [2, 2], [0, 2], [2, 0]])

        if self.board[1][1] == None:
            return [1, 1]

        return None



'''def bot_move(figure):
   bot = bot_choose()
   bot_think=bot_think_move()

   if bot_think!=None:
       try:
            circle.rect.x = choose[bot_think[0]][bot_think[1]][0]
            circle.rect.y = choose[bot_think[0]][bot_think[1]][1]

            choose[bot_think[0]][bot_think[1]] = None
            place_game[bot_think[0]][bot_think[1]] = "O"

            all_sprites.add(circle)
       except Exception:
           pass


   elif bot_think==None and bot!=None:
       index=[]
       for i in range(len(choose)):
           if index!=[]:
               break
           try:
               index=[i, choose[i].index(bot)]
           except:
               pass


       if figure=="circle":
           circle.rect.x = bot[0]
           circle.rect.y = bot[1]

           choose[index[0]][index[1]]=None
           place_game[index[0]][index[1]]="O"


           all_sprites.add(circle)

def bot_choose() -> list[int, int]:
    if [y for y in choose if y != [None, None, None]] != []:
        row = choice([y for y in choose if y != [None, None, None]])
        bot = choice([x for x in row if x != None])
        return bot
    else:
        return equally()

def bot_think_move():
    for number, row in enumerate(place_game):
        if row[0] == row[1] == "O" and row[2] == None:
            return [number, 2]
        elif row[1] == row[2] == "O" and row[0] == None:
            return [number, 0]
        elif row[0] == row[2] == "O" and row[1] == None:
            return [number, 1]

    for i in range(3):
        if place_game[0][i] == place_game[1][i] == "O" and place_game[2][i] == None:
            return [2, i]
        elif place_game[1][i] == place_game[2][i] == "O" and place_game[0][i] == None:
            return [0, i]
        if place_game[0][i] == place_game[2][i] == "O" and place_game[1][i] == None:
            return [1, i]

    if place_game[0][0] == place_game[1][1] == "O" and place_game[2][2] == None:
        return [2, 2]
    elif place_game[1][1] == place_game[2][2] == "O" and place_game[0][0] == None:
        return [0, 0]
    elif place_game[0][0] == place_game[2][2] == "O" and place_game[1][1] == None:
        return [1, 1]

    if place_game[0][2] == place_game[1][1] == "O" and place_game[2][0] == None:
        return [2, 0]
    elif place_game[1][1] == place_game[2][0] == "O" and place_game[0][2] == None:
        return [2, 0]
    elif place_game[0][2] == place_game[2][0] == "O" and place_game[1][1] == None:
        return [1, 1]

    for number, row in enumerate(place_game):
        if row[0] == row[1] == "X" and row[2] == None:
            return [number, 2]
        elif row[1] == row[2] == "X" and row[0] == None:
            return [number, 0]
        elif row[0] == row[2] == "X" and row[1] == None:
            return [number, 1]

    for i in range(3):
        if place_game[0][i] == place_game[1][i] == "X" and place_game[2][i] == None:
            return [2, i]
        elif place_game[1][i] == place_game[2][i] == "X" and place_game[0][i] == None:
            return [0, i]
        if place_game[0][i] == place_game[2][i] == "X" and place_game[1][i] == None:
            return [1, i]

    if place_game[0][0] == place_game[1][1] == "X" and place_game[2][2] == None:
        return [2, 2]
    elif place_game[1][1] == place_game[2][2] == "X" and place_game[0][0] == None:
        return [0, 0]
    elif place_game[0][0] == place_game[2][2] == "X" and place_game[1][1] == None:
        return [1, 1]

    if place_game[0][2] == place_game[1][1] == "X" and place_game[2][0] == None:
        return [2, 0]
    elif place_game[1][1] == place_game[2][0] == "X" and place_game[0][2] == None:
        return [2, 0]
    elif place_game[0][2] == place_game[2][0] == "X" and place_game[1][1] == None:
        return [1, 1]

    if place_game[0][0] == place_game[1][1] == "X" and place_game[2][2] == "O":
        return choice([[2, 0], [0, 2]])
    elif place_game[1][1] == place_game[2][2] == "X" and place_game[0][0] == "O":
        return choice([[0, 2], [0, 2]])

    if place_game[0][2] == place_game[1][1] == "X" and place_game[2][0] == "O":
        return choice([[0, 0], [2, 2]])
    elif place_game[1][1] == place_game[2][0] == "X" and place_game[0][2] == "O":
        return choice([[0, 0], [2, 2]])

    if place_game[0].count(None) == 3 and place_game[1].count(None) == 2 and place_game[2].count(None) == 3 and place_game[1][1] == "X":
        return choice([[0, 0], [2, 2], [0, 2], [2, 0]])

    if place_game[1][1]==None:
        return [1, 1]
    return None'''
