import os, random

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls')


# playerChoice = ["kick", "headbump", "punch", "quit", "k", "p", "h"]
playerChoiceDict = {"kick": 1, "k": 1, "headbump": 2, "h": 2, "punch": 3, "p": 3, "quit": 4, "settings": 5, "s": 5}  # used
settingsDict ={"close settings": 1, "close": 1, "instructions": 2}
playerHealth = 20  # used
enemyWave = 0  # implemented
enemyHealth = 3  # implemented
healPercent = 30  #
critPercent = 20  #
playerMaxCrit = 3  #
playerMoveCount = 0  #

kickWinWords = ["oooh, that was a great kick", "omg, you kick em really hard", "you didn't need to kick em this hard"]
headbumpWinWords = ["oooh, that was a great headbump", "omg, you bashed your head into him really hard", "is your head ok after this headbump"]
punchWinWords = ["oooh, that was a great punch", "omg, you punched em really hard", "you don't need to punch em so hard"]

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
        self.enemyHealth = 3

    def enemyMoveSet(self):
        self.enemyMove = random.randrange(0, 3)
        return self.enemyMove

    def enemyMoveGet(self):
        return self.enemyMove

    def enemyHealthGet(self):
        return self.enemyHealth

    def playerHealthSet(self):
        pass  # TODO make the wave thing



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

    def playerHealthGet(self):
        return self.playerHealth


class Game:
    def __init__(self):
        self.gameState = "game"
        self.theDiceRolled = None
        self.theSettings = {"instructions": True, }  # add more settings

    def instructions(self):
        if self.gameState == "game":
            print(self.theSettings["instructions"] and "You can use kick, headbump, punch \n kick > headbump \n headbump > punch \n punch > kick")

    def gameStateGet(self):
        return self.gameState

    def theDice(self):
        if self.gameState == "game":
            if p.playerMoveGet() == 1 or p.playerMoveGet() == 2 or p.playerMoveGet() == 3:

                if p.playerMoveGet() > e.enemyMoveGet() and not (p.playerMoveGet() == 3 and e.enemyMoveGet() == 1):
                    self.theDiceRolled = "win"
                    print("you win")
                elif p.playerMoveGet() == e.enemyMoveGet():
                    self.theDiceRolled = "draw"
                    print("draw")
                else:
                    self.theDiceRolled = "loss"
                    print("you lose")

            elif p.playerMoveGet() == 4:  # 4 == quit
                self.theDiceRolled = "quit"

            elif p.playerMoveGet() == 5:  # 5 == setting
                game.settings("opening")

            else:
                print("wrong input, try again, you idiot")


            # TODO here should be something more but i don't know what
        elif game.gameState == "settings":
            game.settings(input())

    def theDiceRoll(self):
        return

    @staticmethod
    def playerHealthDisplay():
        print("Your health is " + str(p.playerHealthGet()))

    @staticmethod
    def enemyHealthDisplay():
        print("Enemy health is " + str(e.enemyHealthGet()))

    def settings(self, whichSetting):
        # print("What you want to change?")
        # game.settingsDisplay()
        # self.gameState = "settings"
        # if whichSetting == 1:  # whichSetting 1 == close
        #     self.gameState = "game"
        # elif whichSetting == 2:  # this is instructions toggle
        #     # if self.theSettings["instructions"]:
        #     #     self.theSettings["instructions"] = False
        #     # elif not self.theSettings["instructions"]:
        #     #     self.theSettings["instructions"] = True
        #     #
        #     # self.theSettings["instructions"] = not self.theSettings["instructions"]
        #     self.theSettings["instructions"]^=True






    def settingsDisplay(self):
        print("You can use close to close the settings")
        for key, value in self.theSettings.items():
            if value:
                temp = "ON"
            elif not value:
                temp = "OFF"

            print(key + " is " + temp)




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
    # TODO add cls() somewhere
    game.instructions()
    if game.gameStateGet() == "settings":
        pass
    else:
        p.playerMoveTake(input())
    e.enemyMoveSet()
    theDice = game.theDice()







