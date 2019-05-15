
# Dominic Adamson
# Put a date here
# Programming Class Python Battleship Game

# I have built the basic layout of a Battleship style game
# for you.  There are several functions that need to be
# built before it will work.  Fill in those functions to
# complete the game.

# You are going to need this
import random,sys,os,time

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

# While testing your code, leave this at True
# When you are ready to play, change it to False
# It will hide the ships location from the player
testing = True

height,length,board,shipRow,shipColumn = '','','','',''
# Create the basic board
# This can be done as you wish, since you will be working
# with your own board in the other functions.  It is
# suggested to make a 2D array (a list of lists), but could
# really be done in many ways.  I made a list of 5 "0", then
# made a list of 5 of those lists, giving me a 5x5 board to
# play on.  Make your board at least 3x3.  From there, it is
# up to you.
# Return the board.
def createBoard(height=5,length=5):
    board = [["0"] * height for i in range(length)]
    return board


# Print the board
# Use this function to print out your board in a nice looking
# way.  The user will see this each turn.  If you are using
# lists, the " ".join(listName) will probably be helpful.  If
# you are using some other way to make your board, have fun!
# Return nothing (it is a print function)
def printBoard(board):
    for item in board:
            print(" ".join(item))
    return


# Randomly place a ship
# Have the computer pick where to place the ship in a
# random location.  As I have imported the random library
# for you, you have access to functions such as random.randint(a,b)
# that will be of great help.  Make sure your ship is within
# your board size.
# Return shipCoordinate1, shipCoordinate2
def placeShip(board,height,length):
    x = random.randint(0,height-1)
    y = random.randint(0,length-1)
    return x, y


# Mark a spot on the board as the ship
# Given a row and column, mark the spot on the board as a ship.
# You may choose some symbol to represent this, or some other
# method.  If your board is a list of lists, you can access
# specific parts of the board using the [a][b] notation.
# Return the marked board
def markShip(board, row, col):
    board[row][col] = "S"
    return board


# Mark a spot on the board as a miss
# Given a row and column, mark the spot on the board as a miss.
# You may choose some symbol to represent this, or some other
# method.  If your board is a list of lists, you can access
# specific parts of the board using the [a][b] notation.
# Return the marked board
def markMiss(board, row, col):
    board[row][col] = "M"
    return board


# Mark a spot on the board as a hit!
# Given a row and column, mark the spot on the board as a hit.
# You may choose some symbol to represent this, or some other
# method.  If your board is a list of lists, you can access
# specific parts of the board using the [a][b] notation.
# Return the marked board
def markHit(board, row, col):
    board[row][col] = "H"
    return board



# Take a user guess
# Get input from the user for where to attack.
# It is suggested to verify that the attack is actually on the
# board, and report back to the user and be nice (or mean) as
# neccesary.  For example, if they miss the board, should they
# get another shot?
# Return guessCoordinate1, guessCoordinate2
def guess(board,ymax,xmax):
    try:
        x = int(input("What is the X cordinate of your shot "))-1
        y = int(input("What is the Y cordinate of your shot "))-1
        if y <= ymax-1 and y >= 0:
            if x <= xmax-1 and x >= 0:
                return y,x
            else:
                print("Ya Stupid That ain't a Valid X Pos")
                return guess(board,ymax,xmax)
        else:
            print("Ya Stupid That ain't a Valid Y Pos")
            return guess(board,ymax,xmax)
    except:
        print("Thats not a number")
        return guess(board,ymax,xmax)
        

def init():
    global height,length,board,shipRow,shipColumn

    height = clamp(int(input("how tall do you want your board ")),1,25)
    length = clamp(int(input("how long do you want your board ")),1,25)
    board = createBoard(length,height)
    shipRow, shipColumn = placeShip(board,height,length)
    if testing:
        print(shipRow, shipColumn)
        board = markShip(board, shipRow, shipColumn)

    print ("Welcome to Battleship!")
    print()
    numberOfTurns = length*height//5
    return numberOfTurns

def turn(num,numberOfTurns):
    global height,length,board,shipRow,shipColumn
    time.sleep(1) 
    os.system('CLS')
    printBoard(board)
    print ("Turn %i of %i" %(num+1, numberOfTurns))
    guessRow, guessColumn = guess(board,height,length)
    if guessRow == shipRow and guessColumn == shipColumn:
        os.system('CLS')
        board = markHit(board, guessRow, guessColumn)
        print ("Congratulations!  You win!")
        printBoard(board)
        play = input("\nDo you want to play again? y/n\n").lower()
        if play == "y":
            main()
            return
        else:
            sys.exit(1)

    else:
        board = markMiss(board, guessRow, guessColumn)
        print ("You missed")
        if num == numberOfTurns-1:
            play = input("\nDo you want to play again? y/n").lower()
            if play == "y":
                main()
                return
            else:
                sys.exit(1)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# From here down is the basic running part of the game.
# Look it over, try to understand it, but I really don't
# think you should edit it.  (Unless you finished the
# basic assignment and want to have more fun.)
# Look at the very bottom for some extra credit suggestions.
def main():
    global height,length,board,shipRow,shipColumn
    numberOfTurns = init()
    
    for turns in range(numberOfTurns):
        turn(turns,numberOfTurns)
        


if __name__ == '__main__':
  main()
  input("press ENTER to continue")

# Extra credit suggestions:
#
# -Have the game ask if you want to play again.  Do accordingly.+
# -Keep score of wins vs. losses
# -Make the board size a variable for difficulty+
# -Add some other difficulty variable, ask the user how hard
#  to make the game.  Do accordingly.
# -Tell the user if they are close to hitting the ship
# -Make this more like real battleship, with ships of longer
#  length that take more than one hit to sink
# -If a guess is in a location already guess, inform the user
#  and allow a re-try.
# -Make this 2 player
# -Make this 2 player on separate computers
# -Add sound effects
# -Add graphics
# -Bring your teacher a dessert
