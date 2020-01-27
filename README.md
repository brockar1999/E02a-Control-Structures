
# E02a-Control-Structures

Let's start experimenting with some Python code! This is a set of exercises for MSCH-C220; they should give you the tools to help build your first game.
 
This exercise assumes that you have already installed Python, GitHub Desktop, and VS Code, and that you have already created a GitHub account. If that is not the case, please refer to previous exercises.

This repository contains several files that you will need to alter to complete the assignment. Fork this repository (instructions below) and edit the files. Commit and push the changes back to GitHub and turn in the URL to your repository on Canvas.

Comments in Python are marked by a # sign (for single-line comments) or three matching quotation marks (''' or """) if a comment requires more than one line. They should also appear in a different color in VS Code. The Python Interpreter ignores comments, so you can safely include any information you want there.

*If you wish your exercise to be graded, please edit the LICENSE file (add the current year and your name).*

Edit README.md to answer the following questions:

NOTE: I feel like I should mention I'm a CS major, so I know a lot of this stuff, so I'm sorry if my 'expected' answers aren't what you're really looking for! I'm fine with doing these assignments (because they're good Python review), but I wanted to add a disclaimer.

- Open main01.py. Before running it, what do you expect this program to do?
  * The program will print 'Greetings!' and take in input from the question: 'What is my favorite color?'
  - Now right click on the main1.py window and select “Run Python File in Terminal”. Click in the bottom panel, and answer the question. Describe what happened.
    * What I expected.
  - What do you think the program did with what you typed in answer to the question?
    * There was no variable in which to store that information, so it didn't save it at all.
- Open main02.py. Before running it, describe how this is different than main01.py.
  * It stores the answer in a variable and then prints that variable.
  - What do you think the color = input() will do?
    * Will store the answer in the variable
  - Run the program in the terminal and answer the question. Did the program do what you expected?
    * Yes.
- Open main03.py. Before running it, describe how this is different than main02.py.
  * There's an if-else statement.
  - What is happening on lines 9–12?
    * If the color is red, then the program prints 'Correct!' If not, it prints something else.
  - Why are lines 10 and 12 indented?
    * They are part of an if or else statement-- the parts indented are what happen if the condition(s) are met.
  - Run the program and answer the question. What happens if you don’t capitalize Red?
    * It's not correct.
  - What does this tell you about "color"?
    * It's case-sensitive.
- Open main04.py. Before running it, describe how this is different than main03.py.
  * There's an OR in the if-statement.
  - What problem is this trying to solve?
    * The possibility of someone inputting 'red'.
  - Run the program and answer the question. What happens if you use some other capitalization scheme (i.e., “RED” or “reD“)?
    * Still not correct.
- Open main05.py. What do you expect line 9 to do?
  * Put the inputted string into lowercase.
  - What problem is it trying to solve?
    * People who don't enter a case-sensitive 'Red'.
  - Run the program and answer the question. What happens if you add spaces before or after the word (i.e., “ RED “ or “ red”)?
    * Still not correct.
 - Open main06.py. How is line 9 different than in main05.py?
  * The addition of ".strip()".
   - What would you guess .strip() is doing?
    * Removing the spaces on the ends.
   - Run the program and answer the question. Is there another way of writing “red” that will break this logic?
    * Adding spaces within the word. i.e. 'r e d'
 - Open main07.py. Before running this program, how do you expect this to be different than main06.py?
  * There's an added condition.
   - What is happening on line 12?
    * An added condition for 'pink'.
   - Run the program and answer the question.
    * There are now three possible outcomes for the program.
 - Open main08.py. What is the purpose of line 9?
  * Setting a count variable.
   - Why are lines 10–17 indented?
    * They are within the while-loop.
   - Run the program. What would happen if line 10 were moved before line 9 (and no longer indented)?
    * color would never change.
   - Make that change and run the program again. (To end any Python program, you can type ctrl-c)
    * Yup.
 - Open main09.py. What is happening on line 13?
  * count is being incremented.
   - What is the purpose of “count”?
    * Counting how many times the loop iterates/how many guesses the person makes.
   - What is happening on line 22?
    * There is no line 22. If you're talking about 21, then the program is displaying how many times the user guessed using the count variable.
   - Run the program.
    * Okeedokee.
 - *Extra credit:* open main10.py. Add a comment to each line describing what it is doing (a comment follows a pound sign [#]).
  * Sure thing.
 - *Extra credit:* open main11.py. What is happening on lines 6-11?
  * A function generating a new color until a color that does not match the last color is generated.
  
Commit your changes and push them back to the repository.
 

---

Instructions for forking this repository:
 
Log into your account on [github.com](https://github.com)

Go to the [exercise template page](https://github.com/BL-MSCH-C220-S20/E02a-Control-Structures) on GitHub

There is a button in the top right corner of the page labeled "Fork". Press that now

This will create an independent copy of this repository in your account that you can control and edit

Go to your GitHub home page, and select the new E02a-Control-Structures repository

On that page, you will see a green button labeled "Clone or download". Press that now. You will see a drop down box. Press the "Open in Desktop" button.

This should launch GitHub Desktop. It will ask you for a location (on your computer) where the repository may be cloned (downloaded). Choose a location that will be easy for you to find, and press the blue "Clone" button.

Once GitHub Desktop has cloned (downloaded) the code, it will be responsible for keeping the code on your local computer synchronized with the repository in your GitHub account. Now, open Visual Studio Code, and choose File->Open. Find the folder of the cloned repository and select Open.

In the left (File Explorer) panel, you should see a list of files that comprise this repository

First, edit the file called LICENSE. Replace year and name with the current year and your name. Save this file

Then open README.md. Feel free to remove any extraneous information, and then answer the questions posed in the file. You can add your answers after each question

When the time comes for you to run any of the python files, you can do so by clicking the green arrow in the top right corner of the window or by right-clicking on the code and selecting "Run Python File in Terminal". The results will appear at the bottom. If you don't see "Run Python File in Terminal" in the contextual menu, that is because VS Code doesn't have the Python extension installed. You can do that here: [https://marketplace.visualstudio.com/items?itemName=ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

When you are done editing the files, return to GitHub Desktop. In the left panel, you should see a list of the files that have changed

At the bottom of the leftmost area, you should see a text box labeled "Summary (required)". Add a message that describes what you have done; these messages are typically stated in the active-present tense. For example, "Updates the LICENSE, README.md, and completes the assignment." Push the blue "Commit to master" button

In the top bar of the window, you should see a button that is labeled "Push origin", push that now

Check out your page on GitHub. You should see the changes you made reflected there, Repeat steps 10 through 16 as necessary

When you are satisfied with your efforts, turn in a URL to your repository on Canvas

---
If you try to push your changes, and you receive a permission error, it is likely that you are trying to edit the BL-MSCH-C220-S20 copy of the repository rather than your own. Make sure you don't skip the step of forking your own copy and cloning that.

---

The grading criteria will be as follows:
 
[1 point] Repository contains a description of the project in README.md

1 point will be awarded for answering the questions associated with each of the files

10 points total (+2 points extra credit)
