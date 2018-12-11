# Rock, paper, scissors game B05:
from random import randint # Allows the generation of random numers, "randint" means random integer 

# Lets define some values
player_score = 0
computer_score = 0
x = player_score
y = computer_score

# Using a dictionary with winning results makes for a much cleaner results section.
Outcomes = {'Rock':'Scissors',
          'Paper':'Rock',
          'Scissors':'Paper'
        }
# Here were set the name of the while loop and set it's value to 0, we add 1 each time the loop runs until it gets to 4 where the loops ends.
Best_of_five = 0 
while Best_of_five <= 4:
    Best_of_five += 1 
    # Here we add a prompt for the player to input a value, rememeber \n just makes the code start on a new line. 
    player = input("\nRock, Paper or Scissors? :")
    print(player, "\nVs.") 
    # The players input is printed and then the computer is asked to pick a number between 1 and 3. These numbers are given values and those values are printed.
    chosen = randint(1, 3)
    if chosen == 1:
        computer = "Rock"
    elif chosen == 2:
        computer = "Paper"
    else:
        computer = "Scissors"
    print(computer)
    # This section determines what results we get from the input. If the input from the player and computer are the same its a draw.
    # The "Outcomes" dictionary holds the possible winning combinations for the player. What is left over will be losing combinations for the player.
    # Points are awarded to who wins anda running tally is kept. The current scores are also printed.
    if player == computer:
        print("\nTie \nComputer: " + str(y) + " Player: " + str(x))
    elif Outcomes.get(player) == computer:
        x += 1
        print("\nYou win! \nComputer: " + str(y) + " Player: " + str(x))
    else:
        y += 1
        print("\nComputer wins! \nComputer: " + str(y) + " Player: " + str(x))
# Once there have been 5 loops of the game this else statement will figure out the winner through a series of greater than or less than statements.
# Remember that "x" is the player and "y" is the computer and depending on who wins the rounds one point is added.
else:
    if x > y:
        print("\nWINNER WINNER CHICKEN DINNER!")
    elif y > x:
        print("\nBETTER LUCK NEXT TIME, SKYNET WINS!")
    else:
        print("\nITS A DRAW!")
