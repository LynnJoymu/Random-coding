# Lynn-Joy Murray
# Holiday coding cause why not

import random
import numpy as np
import matplotlib.pyplot as plt

### PART 1: Rock, Paper, Scissors ###

hand = ['rock', 'paper', 'scissors']

prog_tally = 0
opp_tally = 0

for i in range(5):
    prog_hand = random.choice(hand)
    opp_hand = input("Please choose rock, paper, or scissors: \n")
    
    print("Program chose:", prog_hand, "\nUser chose:", opp_hand)
    
    if opp_hand == 'rock':
        if prog_hand == 'rock':
            print("Oh! It's a tie!")
        elif prog_hand == 'paper':
            print("Paper beats Rock!")
            prog_tally += 1
        elif prog_hand == 'scissors':
            print("Rocks beats Scissors!")
            opp_tally += 1

    elif opp_hand == 'paper':
        if prog_hand == 'paper':
            print("Oh! It's a tie!")
        elif prog_hand == 'scissors':
            print("Scissors beats Paper!")
            prog_tally += 1
        elif prog_hand == 'rock':
            print("Paper beats Rocks!")
            opp_tally += 1

    elif opp_hand == 'scissors':
        if prog_hand == 'scissors':
            print("Oh! It's a tie!")
        elif prog_hand == 'rock':
            print("Rocks beats Scissors!")
            prog_tally += 1
        elif prog_hand == 'paper':
            print("Scissors beats Paper!")
            opp_tally += 1
    
    else:
        print("That's not an option... Didn't you play this game as a child dummie?")
        break

if prog_tally == opp_tally:
    print("It's a tie! Try again.")
elif prog_tally > opp_tally:
    print("The winner is the python programme! Try again.")
elif prog_tally < opp_tally:
    print("The winner is you, User! Well done!")


### PART 2: Plot the function ###

colour = ['red', 'orange', 'mediumseagreen', 'blue', 'purple']           ### set custom colours for each subplot; colours found at: https://matplotlib.org/stable/users/explain/colors/colors.html#sphx-glr-users-explain-colors-colors-py

x = np.linspace(0, 10, 500)

y1 = np.sin(x)
y2 = np.abs(x - 5)
y3 = x**3 - 3*x + 2
y4 = np.exp(x)
y5 = x**3 + 2*x**2 -7*x + 2
y = [y1, y2, y3, y4, y5]

fig, ax = plt.subplots(5, 1, sharex=False, figsize=(7, 14)) 

for j in range(5):
    
    ax[j].plot(x, y[j], color=colour[j])
    ax[j].set_xlabel('x')
    ax[j].set_ylabel('y')
    ax[j].set_title(f'Function {j+1}')
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.2, hspace=0.7)    ### got the syntax from the following website: https://stackoverflow.com/questions/6541123/improve-subplot-size-spacing-with-many-subplots

plt.show()

### PART 3: Conclusion of Day 1 ###

print("\nThat concludes Lynn-Joy Murray's holiday coding Day 1. Please stay tuned for more days....\nIf there even is! Mwah-ha-ha-ha!")