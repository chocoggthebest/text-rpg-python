import os, random

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls')


# playerChoice = ["kick", "headbump", "punch", "quit", "k", "p", "h"]  # TODO make the input work with only 1 char
playerChoiceDict = {"kick": 1, "k": 1, "headbump": 2, "h": 2, "punch": 3, "p": 3, "quit": 4, "settings": 5}  # used
playerHealth = 20  # used
enemyWave = 0  # implemented
enemyHealth = 3  # implemented
healPercent = 30  #
critPercent = 20  #
playerMaxCrit = 3  #
playerMoveCount = 0  #

kickWinWords = ["oooh, that was a great kick", "omg, you kick em really hard", "you didn't need to kick em this hard"]
headbumpWinWords = ["oooh, that was a great headbump", "omg, you bashed your head into him really hard","is your head ok after this headbump"]
punchWinWords = ["oooh, that was a great punch", "omg, you punched em really hard","you don't need to punch em so hard"]

# functions block
# class enemyMove:
#     def __init__(self):
#         self.enemyMove = random.randrange(0, 3)

#     def getMove(self):
#         return enemyMove

# enemyMove = 0
# def enemyMoveCreate():
#     enemyMove = random.randrange(0, 3)
#     return enemyMove
# def enemyMoveGet():
#     return enemyMove

class Enemy:
    def __init__(self):
        self.enemyMove = 0
        self.enemyWave = 0

    def enemyMoveTake(self):
        self.enemyMove = random.randrange(0, 3)
        return self.enemyMove

    def enemyMoveGet(self):
        return self.enemyMove



class Player:
    def __init__(self):
        self.userInput = None
        self.playerMove = 0
        self.playerHealth = 20
        self.playerMoveCount = 0  # TODO make that work

    def playerMoveTake(self, userInput):
        try:
            self.playerMove = playerChoiceDict[userInput]
        except KeyError:
            self.playerMove = 0
        return

    def playerMoveGet(self):
        return self.playerMove

class Game:
    def __init__(self):
        pass

    def instructions(self, instructions):
        print(instructions and "You can use kick, headbump, punch \n kick > headbump \n headbump > punch \n punch > kick")


    def theDice(self):
        if p.playerMoveGet() == 1 or p.playerMoveGet() == 2 or p.playerMoveGet() == 3:

            if p.playerMoveGet() > e.enemyMoveGet() and not (p.playerMoveGet() == 3 and e.enemyMoveGet() == 1):
                print("you win")
                return "w"

            elif p.playerMoveGet() == e.enemyMoveGet():
                print("draw")
                return "d"
            else:
                print("you lose")
                return "l"
        elif p.playerMoveGet() == 4:
            return "q"

        elif p.playerMoveGet() == 5:
            pass  # TODO go to settings
        else:
            print("wrong input, try again, you idiot")
            # TODO here should be something more but i don't know what

    def settings(self):
        pass  # TODO do settings menu or something



# ///
# asd = player()
# asd.playerMoveTake()
# print(asd.playerMoveGet())
# ///


# the main loop
p = Player()
e = Enemy()
game = Game()

while playerHealth > 0:
    p.playerMoveTake(userInput = input())
    e.enemyMoveTake()
    cls()
    theDice = game.theDice()

    game.instructions()  # TODO fill in the instructionsON thing






