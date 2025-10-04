from random import randrange
import os
import csv

leaderboard = []



def checkForFile():
  if os.path.exists("leaderboard.csv"):
    return True
  else:
    open("leaderboard.csv", "x")
    return True


def showScores():
  if checkForFile():
    with open("leaderboard.csv") as file:
      reader = csv.DictReader(file)
      for line in reader:
        score = {"player": line['name'], "rounds": line['guesses'], "range":line['max']}
        leaderboard.append(score)
    try:
      for score in sorted(leaderboard, key=lambda score: (-int(score["range"]), score["rounds"])):
          print(f"{score['player']}: {score['rounds']} guesses. In the range {score['range']}.")
      if line['name'] in leaderboard:    
        pass
    except UnboundLocalError:
      print("\n The leaderboard is empty")

def addScore(name,score,range):
  if checkForFile():
    with open("leaderboard.csv", "a") as file:
      file.write(f"{name},{score},{range}\n")

def play():
  notExit = True
  notWin = False
  try:
    viewOrPlay = int(input("Do you want to view the leaderboard (1) or play (2)?\n"))
  except:
    print("Error: Please enter a valid integer\n")
  try:
    if viewOrPlay == 1:
      showScores()
      
    elif viewOrPlay == 2:
      score = 0
      try:
        playerMax = int(input("Pick the max number!\n"))
      except:
        print("Please enter a valid number.")
      number = randrange(1,playerMax)
      notWin= True
    else:
      print("Please enter (1) or (2)\n")
  except:
    print("Please enter (1) or (2)\n")
  while notWin:
    
    try:
      playerPick = int(input(f"Pick a number from 1 to {playerMax}!\n"))
      if playerPick == number:
        while notExit:
          try:
            name=input("You win! Enter you name to save score: ")
            if("," not in name):
              addScore(name, score, playerMax)
              showScores()
              notExit = False
            elif("," in name):
              print("Please do not use symbols in your name.")
          except:
            print("Please enter a valid name.")
          notWin = False
          
        
      elif playerPick >= number:
        print("Too big...")
        score+=1
        continue
      elif playerPick <= number:
        print("Too small...")
        score+=1
        continue
      
    except: print("Please enter valid numbers.\n")
  
play()
