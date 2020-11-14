import random
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls')


# the var blocks
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

# the big things
while playerHealth > 0:

    if enemyHealth > 0:
        print("You can use kick, headbump, punch \n kick > headbump \n headbump > punch \n punch > kick")

        didHeal = 0
        userInput = input()
        # try:
        #     playerMove = playerChoice.index(UserInput) + 1
        # except ValueError:
        #     playerMove = 0
        enemyMove = random.randrange(0, 3)
        try:
            playerMove = playerChoiceDict[userInput]
        except KeyError:
            playerMove = 0

        if playerMove == 1 or playerMove == 2 or playerMove == 3:  # the the move check

            if playerMove > enemyMove and not (playerMove == 3 and enemyMove == 1):  # the win condition

                if playerMove == 1:  # 1 == kick
                    cls()
                    kickRanIndex = random.randrange(0, len(kickWinWords))
                    print(kickWinWords[kickRanIndex])


                elif playerMove == 2:  # 2 == headbump
                    cls()
                    headbumpRanIndex = random.randrange(0, len(headbumpWinWords))
                    print(headbumpWinWords[headbumpRanIndex])

                elif playerMove == 3:  # 3 == punch
                    cls()
                    punchRanIndex = random.randrange(0, len(punchWinWords))
                    print(punchWinWords[punchRanIndex])

                else:  # if it gets to here it's really really bad
                    print("fuck")

                enemyHealth -= 1
                chance_to_heal = random.randrange(0, 100)
                if chance_to_heal <= healPercent and playerHealth >= 20:
                    playerHealth += 1
                    didHeal = 1
                    cls()
                    print("You manage to heal 1 HP... yey")

                critChance = random.randrange(0, 100)
                if critChance >= critPercent:
                    critHit = random.randrange(1, playerMaxCrit)
                    cls()
                    if didHeal:
                        print("You manage to heal 1 HP... yey")
                    print("dawn you crit that for " + str(critHit + 1))
                    enemyHealth -= critHit

                print(not enemyHealth <= 0 and "Your health is " + str(playerHealth))  # TODO fix this shit nigga
                print(not enemyHealth <= 0 and "Enemy health is " + str(enemyHealth))

            elif playerMove == enemyMove:
                cls()
                print("draw")
                print("You both don't take damage")
                print("Your health is " + str(playerHealth))
                print("Enemy health is " + str(enemyHealth))

            else:
                cls()
                print("You took a hit... -1 hp")
                print("Your health is " + str(playerHealth))
                print("Your health is " + str(playerHealth))
                playerHealth -= 1

        elif playerMove == 4:
            print("not cool bro")
            break

        else:
            cls()
            print("wrong input, try again, you idiot")
            print("Your health is " + str(playerHealth))
            print("Enemy health is " + str(enemyHealth))

    else:
        enemyHealth = 3
        print("You killed the enemy, the next one is coming at ya")
