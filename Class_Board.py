import random
import sys
import os
import time
import replit

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)
def clear():
        os.system("CLS")
        replit.clear()
testing = False
wins = [0,0]
winsOther = [0,0]

boardYours, boardEnemy = '',''

def printBoards(board1,board2):
    time.sleep(1)
    clear()
    x = 0
    if len(board1) <= 7:
        space = len(board1[0])*2 - 0
        spaces = (" " * space)

        print("player2's board"+spaces+"player1's board")
        for item in board1:
            print(" ".join(item)+"                "+" ".join(board2[x]))
            x+=1
    else:
        space = len(board1[0])*2 - 11
        spaces = (" " * space)

        print("player2's board"+spaces+"player1's board")
        for item in board1:
            print(" ".join(item)+"     "+" ".join(board2[x]))
            x+=1

class Board:
    def __init__(self, height=5, length=5, dif=5, mark=False):
        
        self.height = height
        self.length = length
        self.board = [["0"] * self.height for i in range(self.length)]
        self.shipRow, self.shipColumn = self.placeShip()
        
        self.dif = dif
        self.numberOfTurns = self.length*self.height//self.dif + 1

        self.player = "regular"
        if mark:
            print(self.shipColumn+1, self.shipRow+1)
            self.board = self.markShip(self.shipRow, self.shipColumn)
            self.player = "other"
    

    def printBoard(self):
        for item in self.board:
            print(" ".join(item))
        return

    
    def placeShip(self):
        y = random.randint(0,self.height-1)
        x = random.randint(0,self.length-1)
        return x,y
    

    def markShip(self, row, col):
        self.board[row][col] = "S"
        return self.board

    
    def markMiss(self, row, col):
        self.board[row][col] = "M"
        return self.board

    
    def markHit(self, row, col):
        self.board[row][col] = "H"
        return self.board

    
    def hideShip(self):
        self.board[self.shipRow][self.shipColumn] = "0"
        return self.board
    

    def showShip(self):
        self.board[self.shipRow][self.shipColumn] = "S"
        return self.board


    def guess(self):
        ymax = self.height-1
        xmax = self.length-1
        try:
            x = int(input("What is the X cordinate of your shot "))-1
            y = int(input("What is the Y cordinate of your shot "))-1
            if y <= ymax and y >= 0:
                if x <= xmax and x >= 0:
                    if self.board[y][x] == "M":
                        print("Hey Stupid Ya Already Shot There")
                        return self.guess()
                    return y,x
                else:
                    print("Ya Stupid That ain't a Valid X Pos")
                    return self.guess()
            else:
                print("Ya Stupid That ain't a Valid Y Pos")
                return self.guess()
        except:
            print("Thats not a number")
            return self.guess()


    def turnEnemy(self,num):
        global wins
        guessRow = random.randint(0,self.height-1)
        guessColumn = random.randint(0,self.length-1)

        if self.board[guessRow][guessColumn] == "M":
            self.turnEnemy(num)

        if guessRow == self.shipRow and guessColumn == self.shipColumn:
            self.board = self.markHit(guessRow,guessColumn)
            print("You lose because The enemy shot your ship")
            wins[1] += 1
            print("you have won %i times and lost %i times" %(wins[0],wins[1]))
            play = input("\nDo you want to play again? y/n\n").lower()
            if play == "y":
                clear()
                main()
            else:
                sys.exit(1)
        else:
            self.board = self.markMiss(guessRow,guessColumn)
            #self.printBoard()


    def turnPlayer(self, num):
        global wins
        #time.sleep(1) 
        #clear()
        #self.printBoard()
        print ("Turn %i of %i" %(num+1, self.numberOfTurns))
        guessRow, guessColumn = self.guess()

        if guessRow == self.shipRow and guessColumn == self.shipColumn:
            #clear()
            self.board = self.markHit(guessRow, guessColumn)
            print("Congratulations!  You win!")
            #self.printBoard()
            if self.player == "other":
                wins[1] += 1
                winsOther[0] += 1
                print("you have won %i times and lost %i times" %(wins[0],wins[1]))
            else:
                wins[0] += 1
                winsOther[1] += 1
                print("you have won %i times and lost %i times" %(wins[0],wins[1]))
            play = input("\nDo you want to play again? y/n\n").lower()
            if play == "y":
                clear()
                main()
            else:
                sys.exit(1)
            
        else:
            self.board = self.markMiss(guessRow, guessColumn)
            print ("You missed")
            if (num == self.numberOfTurns-1):
                #clear()
                print("you lose")
                if True:
                    print("The ship was at X: %i Y: %i" %(self.shipColumn+1, self.shipRow+1))
                    self.board = self.markShip(self.shipRow, self.shipColumn)
                #self.printBoard()
                wins[1] += 1
                print("you have won %i times and lost %i times" %(wins[0],wins[1]))
                play = input("\nDo you want to play again? y/n\n").lower()
                if play == "y":
                    #clear()
                    main()
                    return
                else:
                    sys.exit(1)


def init():

    height = clamp(int(input("how tall do you want your board ")),1,777)
    length = clamp(int(input("how long do you want your board ")),1,777)
    dif = int(input("how hard do you want it (bigger is harder) "))
    boardYours = Board(height,length,dif)
    boardEnemy = Board(height,length,dif,True)

    print ("Welcome to Battleship!")
    return boardYours, boardEnemy

def main():
    global boardYours, boardEnemy
    boardYours, boardEnemy = init()
    for turn in range(boardYours.numberOfTurns):
        
        printBoards(boardYours.board,boardEnemy.board)
        print("player1's turn")
        boardYours.turnPlayer(turn)
        boardEnemy.hideShip()
        printBoards(boardYours.board,boardEnemy.board)
        time.sleep(3.5)
        boardYours.showShip()

        printBoards(boardYours.board,boardEnemy.board)
        print("player2's turn")
        boardEnemy.turnPlayer(turn)
        boardYours.hideShip()
        printBoards(boardYours.board, boardEnemy.board)
        time.sleep(3.5)
        boardEnemy.showShip()
        
