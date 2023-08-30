from stockfish import Stockfish
import copy

stockfish = Stockfish(path="/home/sean/stockfish/stockfish-ubuntu-20.04-x86-64-avx2")
moveList = []

def lightLED(loc):
    # lights up an LED given a location
    print(loc)

def moveMade():
    # checks if the player has made the move for the bot
    input()

def detectMove():
    # read the sensor matrix
    return input("Move: ")

def makeMove(moveList):
    lightLED(moveList[-1][:2])
    lightLED(moveList[-1][-2:])
    moveMade()

def gameOver():
    # tells the player the game has ended
    exit()

# bot or not
bot = True
# bot vs bot
botVsBot = False
# rating
stockfish.set_elo_rating(3500)

while(True):
    print(stockfish.get_board_visual())
    if botVsBot == False:
        while(True):
            moveList.append(detectMove())
            try:
                stockfish.set_position(moveList)
                break
            except ValueError or AttributeError:
                moveList = copy.deepcopy(moveList[:-1])
    if bot == True:
        try:
            moveList.append(stockfish.get_best_move())
            stockfish.set_position(moveList)
            makeMove(moveList)
        except ValueError:
            gameOver()
    else:
        gameOver()
