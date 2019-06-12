import tkinter as tk
import ticTacToe as ttt

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

boardSize = 3
board = ttt.initializeMatrix(boardSize)
turn = 'x'
counter = 0
gameStart = False
gameOver = False

# Stores row and column so that each Button uses the place function uniquely
class tButton():

    row = None
    col = None

    def __init__(self, row, col):
        self.row = row
        self.col = col
        tk.Button(root,background="#A6C6ED",font=('Comic Sans MS', 30),width=((screen_width-2)//(boardSize*100)),height=((screen_height-2)//(boardSize*150)),name="b"+str(row)+str(col),text=board[self.row][self.col],command = lambda: place(board,self.row,self.col)).grid(row=self.row,column=self.col)
   
# Changes the title of program to winner if there is one     
def setWinner():
    global turn
    if(ttt.checkWin(board)!=" " or counter>=boardSize**2):
        if(counter>=boardSize**2):
            root.title("It's a tie.")
        else:
            turn = 'o' if turn=='x' else 'x'
            root.title("The winner is "+turn)

# Places an x or o on board. Checks that space isnt occupied
def place(board,row,col):
    
    global counter
    global turn
    global gameOver
    # print(board, turn, row, col)

    if(not gameOver):
        if(board[row][col]!=" "):
            pass
            # print("Error in selection. Space is already occupied.")
        else:
            # print(board, turn, row, col)
            ttt.place(board,turn,row,col)
            root.nametowidget("b"+str(row)+str(col)).configure(text=turn)
            turn = 'o' if turn=='x' else 'x'
            turnLabel()
            counter+=1
            # ttt.printBoard(board)
            if(ttt.checkWin(board)!=" " or counter>=boardSize**2):
                gameOver = True
                setWinner()
            
  
# Changes title to the next turn
def turnLabel():
    root.title("It is {}'s turn".format(turn))


# Sets up buttons and layout
def initializeLayout(board):
    for i in range(boardSize):
        for j in range(boardSize):
            tButton(i,j)
    # root.configure().keys()

# Sets up the game
def playGame():
    global board
    initializeLayout(board)
    global gameStart
    gameStart= True

playGame()
root.resizable(False, False)
root.mainloop()
