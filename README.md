# **Connect4 Command Line Interface Game - Project Portfolio 3 - Python**

Connect4 is a Command Line Interface styled interactive game that allows 2 players to play against each other on the same device.Connect4 is based off the popular Connect4 game uses a similar concept of a connecting 4 pieces in a row to win.

You can view the live program here: <a href ='https://cli-connect-four.herokuapp.com/' target="_blank"> Connect 4 CLI game</a>

# Contents

* [Objective](<#objective>)
* [User Experience](<#user-experience-ux>)
  * [Site Aims](<#site-aims>)
  * [User Stories](<#user-stories>)
  * [Site Structure](<#site-structure>)
* [Features](<#features>)
* [Future Features](<#future-features>)
* [Technologies Used](<#technologies-used>)
* [Testing](<#testing>)
  * [Manual Testing](<#manual-testing>)
  * [Bugs Fixed](<#bugs-fixed>)
* [Deployment](<#deployment>)
* [Credits](<#credits>)
* [Acknowledgements](<#acknowledgements>)

# Objective

The aim of this project is to deliver an interactive and engaging command line interface game that is satisfying for the user to play.

[Back to top](<#contents>)

# User Experience (UX)

## Site Aims

* To provide the player with an interactive and engaging game that can be played against another player
* To create a game that encourages the player to play again
* To provide an interactive experience that is easy to navigate and understand
* To provide a clear and appropriate response to any user inputs

## User Stories

The **user** is any person who has an interest in the old school board games like Connect4, and any games that run via command line.

| ID  | ROLE |                                   ACTION                                   |                    GOAL                     |
| --- | :--- | :------------------------------------------------------------------------: | :-----------------------------------------: |
| 1   | USER |            As a user, I want to be able play the Connect4 game             |            So I can can have fun            |
| 2   | USER |    As a user, I want to be able to navigate around the interface easily    | so it doesn't take me out of the experience |
| 3   | USER | As a user, I want to see clearly from the opening screen what the game is  |        So as to avoid any confusion         |
| 4   | USER |       As a user, I want to be able to access game rules and controls       |       So I know how to play the game        |
| 5   | USER |       As a user, I want to be able to start the game when I am ready       |           So I can prepare myself           |
| 6   | USER |               As a user, I want to be able to track my wins                |           So I can improve on it            |
| 7   | USER | As a user, I want to be able to start a new game when the current one ends |   So I can see if I can beat my opponent    |

[Back to top](<#contents>)

## Flowchart - Python Logic

![Connect4 Flowchart](docs/flowchart/connect4-flowchart.png)

# Features

The Connect 4 Command Line Interface game was created to produce a retro style, immersive experience through the use of limited design (due to the nature of Python) and site structure. It has a game like structure with the use of screens and user input to navigate from one screen to another.

## Navigation

  * The programs navigation is done mainly via the use of on screen menus and user input to navigate from one screen to another
  * The user input is handled so as to prompt the users of the correct input needed to move to the screen of choice.

## Welcome Screen

  * The welcome screen is the first screen the user will see when they run the program.
  * Figlet fonts are used to create the Connect 4 title banner that displays in yellow.
  * This banner is also displayed across multiple other screens throughout the program for consistency.
  * The user is greeted by a message explaining the program and explaining how to input values
  * Through the use of print statements and user input, the user can navigate to the Get Started screen or the Rules screen.
  * The user input is validated before proceeding to the next screen.

## Game Rules

* The Game Rules screen can be accessed by the user from the Welcome Screen via user input of '2'.
* Figlet font is used to display the title banner of Game Rules in a red colour to distinguish it from the main title banner.
* A timed scolling up, line by line text goes through the rules of the game in yellow.
* The information about usernames is in a red font so as to stand out as important information.
* Once the end of the rules is reached, user input is required to move on, allowing the user to scroll back and read the rules in their own time if need be.
* Once the user input is validated the user is brought to another menu, allowing the user to choose to go back to the Welcome Screen or move ahead to the Get Started screen.
* This user input is also validated before allowing the user to move ahead.

## Create Username


## Login


## Start Screen


## Game Screen


## Play Again


## High Scores Screen


## Quite Screen



[Back to top](<#contents>)

# Future Features

[Back to top](<#contents>)

# Technologies Used

[Back to top](<#contents>)

# Testing

[Back to top](<#contents>)

## Bugs Fixed

[Back to top](<#contents>)

# Deployment

## To fork the repository on GitHub

A copy of the GitHub Repository can be made by forking the GitHub account. Changes can be made on this copy without affecting the original repository.

1. Log in to GitHub and locate the repository in question.
2. Locate the Fork button which can be found in the top corner, right-hand side of the page, inline with the repository name.
3. Click this button to create a copy of the original repository in your GitHub Account.

## To clone the repository on GitHub

1. Click on the code button which is underneath the main tab and repository name to the right.
2. In the 'Clone with HTTPS' section, click on the clipboard icon to copy the URL.
3. Open Git Bash in your IDE of choice.
4. Change the current working directory to where you want the cloned directory to be made.
5. Type git clone, and then paste the URL copied from GitHub.
6. Press enter and the clone of your repository will be created.

[Back to top](<#contents>)

# Credits

[Back to top](<#contents>)

# Acknowledgements

[Back to top](<#contents>)
