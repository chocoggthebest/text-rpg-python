import os, random


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls')


# playerChoice = ["kick", "headbump", "punch", "quit", "k", "p", "h"]  # TODO make the input work with only 1 char
playerChoiceDict = {"kick": 1, "k": 1, "headbump": 2, "h": 2, "punch": 3, "p": 3, "quit": 4}
playerHealth = 20
enemyWave = 0
enemyHealth = 3
healPercent = 30
critPercent = 20
playerMaxCrit = 3
playerMoveCount = 0

kickWinWords = ["oooh, that was a great kick", "omg, you kick em really hard", "you didn't need to kick em this hard"]
headbumpWinWords = ["oooh, that was a great headbump", "omg, you bashed your head into him really hard","is your head ok after this headbump"]
punchWinWords = ["oooh, that was a great punch", "omg, you punched em really hard","you don't need to punch em so hard"]


while playerHealth > 0:
