import random
import csv
from collections import deque
import time
import sys

deck = []
playerHand = deque()
CPUhand = deque()
drawDeck = []

# Creates the class and the attributes inside of it
class Player:
    def __init__(self,name, win, loss):
        self.name = str(name)
        self.win = int(win)
        self.loss = int(loss)
    
class CPU:
    def __init__(self, win, loss):
        self.win = int(win)
        self.loss = int(loss)
    
class topTrumpCards:
    def __init__(self,name,height,skills,popularity,yearsPlayed):
        self.name = str(name) 
        self.height = float(height)
        self.skills = float(skills)
        self.popularity = float(popularity)
        self.yearsPlayed= float(yearsPlayed)
        
# This shows how the cards will be shown whilst playing (part of the topTrumpCards class).
    def __repr__(self):
        return f"{self.name}, Height: {self.height}, Skills: {self.skills}, Popularity: {self.popularity}, Years Played: {self.yearsPlayed}"

# This is for giving/gaining the other player cards if they win or lose
def CPUToPlayer():
    if CPUhand:
        playerHand.append(CPUhand.popleft())

def playerToCPU():
    if playerHand:
        CPUhand.append(playerHand.popleft())
        
def CPUSendBack():
    if CPUhand:
        x = CPUhand.popleft()
        CPUhand.append(x)
        
def PlayerSendBack():
    if playerHand:
        y = playerHand.popleft()
        playerHand.append(y)
        
def drawedCards():
    if CPUhand:
        drawDeck.append(CPUhand.popleft())
    if playerHand:
        drawDeck.append(playerHand.popleft())
        
# This is for deciding a winner after the player has chosen an attribute to play
def compareCards(compareCPUhand,comparePlayerHand):
    if compareCPUhand < comparePlayerHand:
        time.sleep(1.5)
        print("You won this round, Your turn.")
        CPUToPlayer()
        PlayerSendBack()
        runGame()
    elif compareCPUhand > comparePlayerHand:
        time.sleep(1.5)
        print("CPU won this round, CPU's turn.")
        playerToCPU()
        CPUSendBack()
        time.sleep(5)
        CPUturn()
    elif compareCPUhand == comparePlayerHand:
        time.sleep(1.5)
        print("You have the same stats. Play the next round to win both cards.")
        drawedCards()
        runGame()
    else:
        print("unexpected")

     
# This is for the CPUs turn, choosing the best attribute of the current card
def CPUturn():
    CPUheight = CPUhand[0].height / 208.28
    CPUskills = CPUhand[0].skills / 160
    CPUpopularity = CPUhand[0].popularity / 150
    CPUyearsPlayed = CPUhand[0].yearsPlayed / 28
    print("CPU is choosing a stat to play....")
    time.sleep(1.5)
    if CPUheight > CPUskills and CPUheight > CPUpopularity and CPUheight > CPUyearsPlayed:
        compareCPUhand = CPUhand[0].height
        comparePlayerHand = playerHand[0].height
        print("CPU picks Height.")
        time.sleep(1)
        print("Your card - ", str(playerHand[0].name), "reads:", float(playerHand[0].height))
        print("CPU's card - ", str(CPUhand[0].name), "reads:", float(CPUhand[0].height))
        compareCards(compareCPUhand,comparePlayerHand)
    elif CPUskills > CPUheight and CPUskills > CPUpopularity and CPUskills > CPUyearsPlayed:
        compareCPUhand = CPUhand[0].skills
        comparePlayerHand = playerHand[0].skills
        print("CPU picks Skills.")
        time.sleep(1)
        print("Your card - ", str(playerHand[0].name), "reads:", float(playerHand[0].skills))
        print("CPU's card - ", str(CPUhand[0].name), "reads:", float(CPUhand[0].skills))
        compareCards(compareCPUhand,comparePlayerHand)
    elif CPUpopularity > CPUheight and CPUpopularity > CPUskills and CPUpopularity > CPUyearsPlayed:
        compareCPUhand = CPUhand[0].popularity
        comparePlayerHand = playerHand[0].popularity
        print("CPU picks Popularity.")
        time.sleep(1)
        print("Your card - ", str(playerHand[0].name), "reads:", float(playerHand[0].popularity))
        print("CPU's card - ", str(CPUhand[0].name), "reads:", float(CPUhand[0].popularity))
        compareCards(compareCPUhand,comparePlayerHand)
    else:
        compareCPUhand = CPUhand[0].yearsPlayed
        comparePlayerHand = playerHand[0].yearsPlayed
        print("CPU picks Years Played.")
        time.sleep(1)
        print("Your card - ", str(playerHand[0].name), "reads:" , float(playerHand[0].yearsPlayed))
        print("CPU's card - ", str(CPUhand[0].name), "reads:", float(CPUhand[0].yearsPlayed))
        compareCards(compareCPUhand,comparePlayerHand)

# Opens the csv file and turns it into a dictionary, seperating each row
with open("sportsPlayers.csv", mode ='r',) as csv_file:
    csv_dict = csv.DictReader(csv_file)
    # Uses a loop to add each row to the deck, creating objects for each card
    for row in csv_dict:
        ttcard = topTrumpCards(**row)
        deck.append(ttcard)

# Shuffles the deck, and divides them into the player and cpu hands.
random.shuffle(deck)
playerHand = deque(deck[:15])
CPUhand = deque(deck[15:])


# This will ask and compare the values from the players current card and the cpu card
def runGame():
    while True:
            compare = int(input("Choose a stat to play from - Height (1), Skills (2), Popularity (3), Years Played (4). Your current card is : " + str(playerHand[0]) + ": "))
            if compare == 1:
                print("You have selected Height:\n",str(playerHand[0].name),"is", float(playerHand[0].height),"cm tall." )
                comparePlayerHand = playerHand[0].height
                compareCPUhand = CPUhand[0].height
                print(str(CPUhand[0].name), "is",float(CPUhand[0].height), "cm tall.") 
                compareCards(compareCPUhand,comparePlayerHand)
        
            elif compare == 2:
                print("You have selected Skills:\n", str(playerHand[0].name),"reads:", float(playerHand[0].skills))
                comparePlayerHand = playerHand[0].skills
                compareCPUhand = CPUhand[0].skills
                print(str(CPUhand[0].name),"reads: ",float(CPUhand[0].skills))
                compareCards(compareCPUhand,comparePlayerHand)
        
            elif compare == 3:
                print("You have selected Popularity:\n", str(playerHand[0].name), "reads:", float(playerHand[0].popularity))
                comparePlayerHand = playerHand[0].popularity
                compareCPUhand = CPUhand[0].popularity
                print(str(CPUhand[0].name), "reads: ", float(CPUhand[0].popularity))
                compareCards(compareCPUhand,comparePlayerHand)
            
            elif compare == 4:
                print("You have selected Years Played:\n", str(playerHand[0].name), "reads:", float(playerHand[0].yearsPlayed))
                comparePlayerHand = playerHand[0].yearsPlayed
                compareCPUhand = CPUhand[0].yearsPlayed
                print(str(CPUhand[0].name), "reads: ", float(CPUhand[0].yearsPlayed))
                compareCards(compareCPUhand,comparePlayerHand)
        
            else:
                print("Invalid input! \n Please enter a number between the range 1 - 4")
                
            break      
runGame()