#!/usr/bin/env python3
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!') #printing the given string
colors = ['red','orange','yellow','green','blue','violet','purple'] #creating a list of possible colors
play_again = '' #initializing a play_again variable
best_count = sys.maxsize            # the biggest number

while (play_again != 'n' and play_again != 'no'): #a while-loop that goes until someone enters 'n' or 'no' to the play_again question
    match_color = random.choice(colors) #generating a color from the colors list 
    count = 0 #setting the count variable to 0
    color = '' #initializing color variable
    while (color != match_color): #a while-loop while the color guessed does not match the generated color
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line // asks for input for the color variable
        color = color.lower().strip() #alters the color variable to account for excess spaces/case-sensitivity
        count += 1 #increments count
        if (color == match_color): #if the colors match
            print('Correct!') #you win
        else: #if NOT
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #you don't win and get a reminder of how many guesses you've done
    
    print('\nYou guessed it in {} tries!'.format(count)) #if you matched the colors, it tells you how many times you guessed

    if (count < best_count): #if you beat the 'high score'
        print('This was your best guess so far!') #woohoo!
        best_count = count #updating the high score

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip() #asking if you want to play again

print('Thanks for playing!') #thanking people for playing. how polite!