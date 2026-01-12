def Game(input_board: list[list[str]], event):
    for row in input_board:
        if row[0]==row[1]==row[2]!=None:
            if row[0]=="X":
                return event.won()
            else:
                return event.lose()

    for i in range(3):
        if input_board[0][i]==input_board[1][i]==input_board[2][i]!=None:
            if input_board[0][i]=="X":
                return event.won()
            else:
                return event.lose()
    if input_board[0][0]==input_board[1][1]==input_board[2][2]!=None:
        if input_board[0][0]=="X":
            return event.won()
        else:
            return event.lose()
    if input_board[0][2] == input_board[1][1] == input_board[2][0]!=None:
        if input_board[0][2]=="X":
            return event.won()
        else:
            return event.lose()
    return None

def game_check(input_board: list[list[str]]):
   for row in input_board:
       if row[0]==row[1]==row[2]!=None:
           if row[0]=="X":
               return "won"
           else:
               return "won"


   for i in range(3):
       if input_board[0][i]==input_board[1][i]==input_board[2][i]!=None:
           if input_board[0][i]=="X":
               return "won"
           else:
               return "won"
   if input_board[0][0]==input_board[1][1]==input_board[2][2]!=None:
       if input_board[0][0]=="X":
           return "won"
       else:
           return "won"
   if input_board[0][2] == input_board[1][1] == input_board[2][0]!=None:
       if input_board[0][2]=="X":
           return "won"
       else:
           return "won"
   return None

