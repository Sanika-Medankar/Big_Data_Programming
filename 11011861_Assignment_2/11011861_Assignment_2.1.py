import random
import Cards
import time

cards = Cards.cards

class Player:
    def __init__(self):
        self.playerDeck = []
        self.godspell = False
        self.resurrectSpell = False
        self.score = 0
        self.myturn = False
        self.playerName = ""
        

def game():

    player1 = Player()
    player2 = Player()
    outDatedDeck = []

    def initiatePlayers():
        while not player1.playerName:
            player1.playerName = input("\nEnter player 1 name : ")
        while not player2.playerName:
            player2.playerName = input("\nEnter player 2 name : ")


    def distribute():
        
        random.shuffle(cards)
        for i in range(len(cards)):
            if i % 2 == 0:
                player1.playerDeck.append(cards[i])
            else:
                player2.playerDeck.append(cards[i])
                
    def rollDice():
        print("\nRolling Dice for player {} ...".format(player1.playerName))
        time.sleep(3)
        player1Dice = random.randint(1,6)
        print("\n{}\n\nRolling Dice for player {} ...\n".format(player1Dice, player2.playerName))
        time.sleep(3)
        player2Dice = random.randint(1,6)
        print(player2Dice) 
        return player1Dice, player2Dice             
        
    def startGame():
        nonlocal player1
        nonlocal player2
        nonlocal outDatedDeck
        
        initiatePlayers()

        distribute()
        
        while True:
            player1Dice, player2Dice = rollDice()
            if player1Dice > player2Dice:
                print("\nPlayer {} has higher number on dice.".format(player1.playerName))
                player1.myturn = True
                player2.myturn = False
                break
            elif player2Dice > player1Dice:
                print("\nPlayer {} has higher number on dice.".format(player2.playerName))
                player2.myturn = True
                player1.myturn = False
                break
            else:
                print("\nSame number on both player's dice. Rolling dice for both players again\n")
                continue

        while len(player1.playerDeck) > 0 and len(player2.playerDeck) > 0:
            time.sleep(3)
            print("\nCurrent Scores : \nPlayer {} : {}\nPlayer {} : {}".format(player1.playerName, player1.score,
                                                                       player2.playerName, player2.score))
            if player1.myturn == True:
                player1, player2, outDatedDeck = startWith(player1,player2, outDatedDeck)
            elif player2.myturn == True:
                player2, player1, outDatedDeck = startWith(player2,player1, outDatedDeck)
            
            
    startGame()
    time.sleep(3)
    if player1.score != player2.score:   
        print("\nGame Over\n\nThe Winner is {player} with score {score}\n".format(player = player1.playerName if player1.score > player2.score else player2.playerName,
                                                             score = player1.score if player1.score > player2.score else player2.score))
    else:
        print("\nGame Over\n\nIt's a tie\n")

def startWith(p1, p2, outDeck):
   
    time.sleep(3)
    print("\nRound starts with Player {}\n".format(p1.playerName))
    while True:
        
        option1 = input("\nOptions to start the round :\n\n1. Normal round\n\n{resurrect}0. Quit\n\nEnter your option : "
                        .format(resurrect = "2. Play resurrect spell\n\n" if p1.resurrectSpell == False and len(outDeck) > 0 else ""))
        
        if option1 == "1":
            char = getCharacterictic(p1.playerDeck[-1])# if p1.playerName != "Computer" else generateRandomChar(p1.playerDeck[-1])
            option2 = input("\n1. Continue\n\n{god}0. Quit\n\nEnter your choice : "
                            .format(god = "2. Play God spell\n\n" if p1.godspell == False else ""))

            if option2 == "1":
                while True :
                    optionsFor2 = input("\nOptions for player 2 : \n\n1. Normal round\n\n{resurrect}0. Quit\n\nEnter your choice : "
                                .format(resurrect = "2. Play resurrect spell\n\n" if p2.resurrectSpell == False and len(outDeck) > 0 else ""))
                    if optionsFor2 == "1":
                        p1, p2, outDeck = performNormalRound(p1,p2, outDeck, char)
                        break
                    elif optionsFor2 == "2":
                        p2, outDeck = performResurrect(p2, outDeck)
                        p1, p2, outDeck = performNormalRound(p1,p2, outDeck, char)
                        break
                    elif optionsFor2 == "0":
                        exit()
                    else:
                        print("\nPlease enter a valid input\n")
                        continue
            elif option2 == "2":
                position = int(input("\nEnter the card to be picked up from the top of {} cards in a stack : ".format(len(p2.playerDeck))))
                while True:
                    optionsFor2 = input("\nOptions for player 2 : \n\n1. Normal round\n\n{resurrect}0. Quit\n\nEnter your choice : "
                                .format(resurrect = "2. Play resurrect spell\n\n" if p2.resurrectSpell == False and len(outDeck) > 0 else ""))
                    if optionsFor2 == "1":
                        p1, p2, outDeck = performGodspell(p1,p2, outDeck, char, position)
                        break
                    elif optionsFor2 == "2":
                        p2, outDeck = performResurrect(p2, outDeck)
                        optionsFor1 = input("\nOptions for player 1 : \n\n1. Continue\n\n2. Change the position number\n\nEnter your choice : ")
                        if optionsFor1 == "2":
                            position = int(input("\nEnter the card to be picked up from the top of {} cards in a stack : ".format(len(p2.playerDeck))))
                        elif optionsFor1 == "1":
                            pass
                        else:
                            print("\nPlease enter a valid input")
                        p1, p2, outDeck = performGodspell(p1,p2, outDeck, char, position)
                        break
                    elif optionsFor2 == "0":
                        exit()
                    else:
                        print("\nPlease enter a valid input\n")
                        continue              
            elif option2 == "0":
                exit()
            else:
                print("\nPlease enter a valid input")
                continue
            break
        
        elif option1 == "2":
            p1, outDeck = performResurrect(p1, outDeck)
            char = getCharacterictic(p1.playerDeck[-1])
            optionsFor2 = input("\nOptions for player 2 : \n\n1. Continue\n\n{resurrect}0. Quit\n\nEnter your choice : "
                            .format(resurrect = "2. Play resurrect spell\n\n" if p2.resurrectSpell == False and len(outDeck) > 0 else ""))
            if optionsFor2 == "2":
                p2, outDeck = performResurrect(p2, outDeck)
            elif optionsFor2 == "1":
                pass
            elif optionsFor2 == "0":
                exit()
            else:
                print("\nPlease enter a valid input")
            p1, p2, outDeck = performNormalRound(p1,p2, outDeck, char)
            break
            
        elif option1 == "0":
            exit()
        else:
            print("\nPlease enter a valid input\n")
            continue
    time.sleep(3)             
    return p1, p2, outDeck

def getCharacterictic(p):
    displayCharacteristics(p)
    while True:
        choice = int(input("\nEnter characteristic you want to play for : "))
        if choice == 1 :
            return 'leadership'
        elif choice == 2:
            return 'smartness'
        elif choice == 3:
            return 'goodLooks'
        elif choice == 4:
            return 'swordSkills'
        elif choice == 5:
            return 'politicalSkills'
        else:
            print("\nPlease enter a valid choice\n")
            continue

        
def displayCharacteristics(p):
    print("\n{}\nThe score for the card are : \n\n1. Leadership : {}\n2. Smartness : {}\n3. Good Looks : {}\n4. Sword Skills : {}\n5. Political Skills : {}"
                    .format(p.characterName,
                            p.characterisitcs['leadership'],
                            p.characterisitcs['smartness'],
                            p.characterisitcs['goodLooks'], 
                            p.characterisitcs['swordSkills'], 
                            p.characterisitcs['politicalSkills']))
                    

def performNormalRound(p1,p2, out, char):
    print("\nperforming normal Round")
    displayCharacteristics(p2.playerDeck[-1])
    if p1.playerDeck[-1].characterisitcs[char] > p2.playerDeck[-1].characterisitcs[char]:
        print("\nRound winner : {}".format(p1.playerName))
        p1.score += 1
        p1.myturn = True
        p2.myturn = False
    else:
        print("\nRound winner : {}".format(p2.playerName))
        p2.score += 1
        p2.myturn = True
        p1.myturn = False
        
    out.append(p1.playerDeck[-1])
    out.append(p2.playerDeck[-1])
    del p1.playerDeck[-1]
    del p2.playerDeck[-1]
    
    return p1, p2, out


def performResurrect(p,out):
    print("\nperforming Resurrect")
    randNum = random.randint(0,(len(out) - 1))
    p.playerDeck.append(out[randNum])
    del out[randNum]
    p.resurrectSpell = True
    return p, out


def performGodspell(p1,p2, out, char, position):
    print("\nperforming Godspell")
    while True:
        if (position) <= len(p2.playerDeck) and position > 0:
            break
        else:
            position = int(input("Enter a valid card position to be picked up from the top of {} cards in a stack : ".format(len(p2.playerDeck))))
    displayCharacteristics(p2.playerDeck[-position])
    if p1.playerDeck[-1].characterisitcs[char] > p2.playerDeck[-position].characterisitcs[char]:
        print("\nRound winner : {}".format(p1.playerName))
        p1.score += 1
        p1.myturn = True
        p2.myturn = False
    else:
        print("\nRound winner : {}".format(p2.playerName))
        p2.score += 1
        p2.myturn = True
        p1.myturn = False
        
    out.append(p1.playerDeck[-1])
    out.append(p2.playerDeck[-position])
    del p1.playerDeck[-1]
    del p2.playerDeck[-position]
    p1.godspell = True
    
    return p1, p2, out

    
game()

