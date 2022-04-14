# **Connect4 Command Line Interface Game - Project Portfolio 3 - Python**

Connect4 is a Command Line Interface styled interactive game that allows 2 players to play against each other on the same device.Connect4 is based off the popular Connect4 game uses a similar concept of a connecting 4 pieces in a row to win.

You can view the live program here: <a href ='https://cli-connect-four.herokuapp.com/' target="_blank"> Connect 4 CLI game</a>

![Connect4 Image](docs/images/connect4.png)

# Contents

* [Objective](<#objective>)
* [User Experience](<#user-experience-ux>)
  * [Site Aims](<#site-aims>)
  * [User Stories](<#user-stories>)
  * [Site Structure](<#site-structure>)
  * [Flow Chart](<#flowchart>)
* [Features](<#features>)
* [Future Features](<#future-features>)
* [Technologies Used](<#technologies-used>)
* [Data Model](<#data-model>)
* [Testing](<#testing>)
  * [PEP8 Valdation](<#pep8-validation>)
  * [Manual Testing](<#manual-testing>)
  * [Validation](<#validation>)
  * [Bugs Fixed](<#bugs-fixed>)
  * [Terminal Compatibility](<#terminal-compatibility>)
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

[Back to top](<#contents>)

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

## Flowchart

![Connect4 Flowchart](docs/flowchart/connect4-flowchart.png)

[Back to top](<#contents>)

# Features

The Connect 4 Command Line Interface game was created to produce a retro style, immersive experience through the use of limited design (due to the nature of Python) and site structure. It has a game like structure with the use of screens and user input to navigate from one screen to another.

## Navigation

![Menu example of 4 options](docs/images/play-again-screen.png)

  * The programs navigation is done mainly via the use of on screen menus and user input to navigate from one screen to another
  * For the most part the menu is dictated by numbers e.g. Press 1) To Get Started ...
  * The user input is handled so as to prompt the users of the correct input needed to move to the screen of choice if an incorrect input is entered.


## Welcome Screen

![Welcome Screen](docs/images/welcome-screen.png)

  * The welcome screen is the first screen the user will see when they run the program.
  * Figlet fonts are used to create the Connect 4 title banner that displays in yellow.
  * This banner is also displayed across multiple other screens throughout the program for consistency.
  * The user is greeted by a message explaining the program and explaining how to input values
  * Through the use of print statements and user input, the user can navigate to the Get Started screen or the Rules screen.
  * The user input is validated before proceeding to the next screen.

## Game Rules

![Game Rules screen](docs/images/rules-screen.png)

  * The Game Rules screen can be accessed by the user from the Welcome Screen via user input of '2'.
  * Figlet font is used to display the title banner of Game Rules in a red colour to distinguish it from the main title banner.
  * A timed scolling up, line by line text goes through the rules of the game in yellow.
  * The information about usernames is in a red font so as to stand out as important information.

  ![Important info in red](docs/images/important-info.png)

  * Once the end of the rules is reached, user input is required to move on, allowing the user to scroll back and read the rules in their own time if need be.
  * Once the user input is validated the user is brought to another menu, allowing the user to choose to go back to the Welcome Screen or move ahead to the Get Started screen.
  * This user input is also validated before allowing the user to move ahead.

## Create Username/Login

![Create Username/Login page](docs/images/create-username-login-screen%20-p1.png)

* The get started, one must either create a username or login and this screen can be reached via the Welcome screen and user input ('2') or the Game Rules screen and user input('2')
* The screen itself has the signature Connect 4 title banner in yellow on top.
* Player 1 always starts and is prompted via a user input on whether they would like to create a username('1') or login('2').
* This input is validated.

### Create Username

![Create username screen](docs/images/username-screen.png)
  
  * If the user decides to create a username, they are then prompted to input a username of choice.
  * This input is first converted to all capitals for consistency and to prevent two different usernames such as 'Rhi' and 'rhi' existing.
  * This also future proofs logins for users if they decide to play again, as any mistypes in terms of capitilisation are handled by converting the input to all capitals, avoiding the user potentially mistakenly logging in with someone elses username.
  * Using the .replace() method the user input for username removes any blank spaces from the input so as not to throw an error when appending to google sheets as blank space is translated differently there.
  * The user input is then validated so that:
    1. The length of the string(user input) is not empty
    2. The username itself is between 2 and 10 characters
    3. The user cannot input a username that is already saved in Google Sheets
  * Once the input passes validation, there username is saved in Google Sheets and their Total Wins and Total Loss values are set to 0.
  * The user is greeted with a personalised screen, stating their name, what player they are and what their player piece is and the string is in red for player 1 and yellow for player 2.

  ![Create username validated](docs/images/create_username_success.png)

  * Once Player 1 has input their details, Player 2 is then brought to the same initial on screen menu as player one and if they choose to create a username as well they go through the same steps as player 1.

  ### Player Login

  ![Player login screen](docs/images/p2-login.png)

  * If the user decides to Login, they are then prompted to enter in their username.
  * This input is then first converted to all Capitals in case a user mistypes re capitilisation.
  * The input value is then checked against the usernames already in Google Sheets and if it is there, it will pull that players data into the game and 'log' them in.
  * If it isn't there, the user will be prompted with a message saying Cannot find username and the user can re-enter their username.
  * If Player 2 decides to log in there is an extra step; their input is validated by the above steps but it also checked against Player 1's Username.
    * If it matches the user will be prompted with a message, stating user already logged in, to prevent the same user logging in twice
    * If it doesn't match and the input value found in Google Sheets, then the player data is pulled in for that user and the player 'logged' in.
  * Once validated the username value is matched with that on google sheets and the relevant data pulled into the program; The user's Total Win history and Total Losses history to be displayed when playing the game.
  * The users are greeted with a personalised screen, the same as when a user creates a username

  ![Player login success](docs/images/p2-successful-login.png)

* Once the username data is all validated and the data pulled into the game the users are brought automatically to the next screen which is the start screen.

## Start Screen

![Player start screen](docs/images/start-screen.png)

* The start screen is only accessed in two situations; 
  1. When the users first create usernames/login
  2. Or when the users finish a game and decide to play again they are brought directly to this screen.
* The user is prompted with a message asking them if they are ready and to press 'C' to continue.
* The user input is validated and if passed, gives a countdown of 3, 2, 1 before disappearing and 'PLAY' appears on the screen and the user is brought to the game screen.

## Game Screen

![Game Screen](docs/images/game-screen.png)

* The game screen consists of 3 parts;
  1. The game bar on the top
  2. The 'Game Board' itself
  3. The text for user input and information

  ### Game Bar

  ![Game Bar](docs/images/game-bar.png)

  * The Game bar consists of a number of strings printed together consisting of 
  blank strings and text, with a text highlight (from termcolor and colorama libraries) on all the printed strings to give the illusion of a rectangle.
  * The bar itself has two sets of info on it;
    1. That for the current game which consists of the stats(Player 1s wins and losses and player 2s wins and losses for their game agains each other)
    2. And the history of games played of the two players(Player 1s total wins and losses from whenever the have played the game, and similarly the same for Player 2. )
  * Once a game is won, the game bar is updated immediately and visibly at the end of the game. 
  * The game bar is also utilised in the high scores screen to give the scores related to the current users as well as the verall top scores.

  ### Game Board

  * The game board is a representation of the classic connect 4 game, but larger.
  * It is created through various empty strings and character strings.
  * Visually it looks like a large rectangle split into columns and rows.
  * When a player piece is dropped into the board, like the classic game it fills the next available blank spot to the corresponding column picked.

  ### Player information area

  ![Player 1's turn](docs/images/p1-drop-piece.png)
  ![Player 2's turn](docs/images/p2-drop-piece.png)

  * All player input, error handling and information is printed below the game board.

* Player 1 always starts and is prompted to choose a column between 1 and 10 via user input.
* This input is validated:
  1. To check if the column is free first and if its full it lets the user know and asks them to pick a different one.
  2. To make sure the input they entered is a number and if not prompts the user to make the correct choice
  3. To make sure if the user input is a name, that its between 1 and 10 and if it isn't to prompt the user to make the correct choice. 
* If it passes the player piece (which is a unicode image of a red disc for Player 1 and a yellow disc for Plyer 2), is placed in.
* After every move, the board is checked for a 'win', if there is 4 particular characters in a row either horizontally, vertically or diagonally.
* If not the next player goes and if so the game board is updated with the new results, the players are let know who won.

![Player won the game](docs/images/Player2-winner.png)
* The board isn't wiped immediately allowing the user's to see the winning play.
* To move on requires the user input of 'C' to continue which is validated and if it passes the user continues on to the Play Again screen.
* A tie is also possible, and if all the spaces are filled in the board, the game finishes with the declaration of no winner and the user can continue on to the play again screen.

## Play Again

![Play Again Screen](docs/images/play-again-screen.png)
 
* The play again screen is the screen the user is taken to after they finish a game of connect4.
* From here they are faced with four choices, chosen via user input:
  1. Play Again
  2. Go Back to Welcome Screen - which resets the players without closing the program
  3. Go to the High Scores screen
  4. Exit Game
* Option 1, brings the user straight back to the start screen in a loop, there scores are still present for the current game, te user names are all set and their overall stats are updated no matter how many games they play in the loop.
* Option 2 brings the users back to the welcome screen - effectively resetting the users, allowing for new users to log in and play without exiting the program. Any scores they received in their previous game will have been saved to their overall stats via google sheets and their current game scores will be reset.
* Option 4, takes the users to the high scores screen.
* Option 5, allows the users to exit the program.
* The user input is validated making sure only numbers 1-4 can be selected to progress.

## High Scores Screen

![High Scores Screen](docs/images/high-scores-screen.png)

* High Scores screen can only be accessed from the play again screen (option 3)
* It consists of the game bar on top - the same as that when the game is running
* And the top 5 high scores, sorted by the number of winds in desscending order in table form
* To exit this screen the user must press c to continue.
* The input is validated and if passed brings the user back to the play again screen.

## Quit Screen

![Exit Screen](docs/images/exit-screen.png)

* The exit screen can only be acessed from the play again screen (option 4)
* This shows the user a goodbye message before exiting the program

[Back to top](<#contents>)

# Future Features

## Timer

The timer would add an extra bit of challenge to the user experience and definitely worth implementing as a future feature. Details of the logic flow of the timer can be seen in the [Flowchart](<#flowchart>) section above but it wasn't implemented in the end due to time constraints.

## Single Player Mode

A mode where the user plays against the computer would add a better user experience to the game and appeal to a wider range of people.

## Important Note & Update Security

* Please note that the use of the username only as a system to login is a security risk as players need only see their opponents username and could potentially login as that user. This was done purely to show input error handling while dealing with two different inputs one after the other, and storing and retrieving values associated with those inputs.

Ideally a password would also be used to authenticate a users login, as well as an email address  associatet with the username for retrievals. This could most definitely be a future update but for the moment, the storage of potentially sensitive data was being avoided without some sort of consent from the user and better security.

## Username Flexibility

At the Login section for users, if the user cannot remember their username there is no option to go back to create a username or retrieve a username. This is an important feature to have for better user experience

## Profanity Filter

Make use of a profanity filter when creating usernames.

[Back to top](<#contents>)

# Technologies Used

* HTML5 - to provide some structure to the program
* CSS3 - to provide the styling for the program
* Python - To provide the functionality to the program
* Google Chrome DevTools - Used to debug
* Draw.io - Used to create the flow chart
* Google sheets - used to host the programs data
* VSCode - Used to create, edit and compile the code for the program

## Python Libraries

* gspread - allows communication with Google Sheets
* colorama - allows terminal text to be printed in different colors
* termcolor - can be used in conjunction with colorama for access to an even wider range of colors and tex-highlights
* time - sleep used to pause the program for whatever time uou have determined
* pyfiglet - used to access figlet fonts
* cursor - used to hide the terminal cursor
* sys - used in a function to clear the console
* tabulate - used to format and prettify google sheets data into tables

## VsCode Extensions

* Python
* GitHub Pull and Request
* Markdown all in one
* Draw.io
* Pylance
* Pylance
* Python Indent

[Back to top](<#contents>)

# Data Model

Google Sheets was used to store all the data for the Connect 4 CLI application. Data was sent to and retrieved from it. The google sheet had a singular worksheet which stored all the data. Usernames stored any users created and their relevant stats, linked to their username via columns; their total wins ever at the game and total losses ever at the game.

![Google sheets](docs/images/google-sheets.png)

[Back to top](<#contents>)

# Testing

## PEP8 Validation

[PEP8](http://pep8online.com/) Online validation was used to check that the code is up to standard. All pages cleared the PEP8 validation with no errors.

### run.py

![run.py PEP8 test result](docs/images/run-py-pep8.png)

### validation.py

![validation.py PEP8 test result](docs/images/validation-py-pep8.png)

### visuals.py

![visuals.py PEP8 test result](docs/images/visuals-py-pep8.png)

## Manual Testing

**Note** All inputs have been validated and tested manually. See [Validation](<#validation>)

<details><summary> Manual Testing Info</summary>

### Welcome Screen

  * Verified that the user validation is working correctly
  * Verified that when the user presses '1' and 'Enter', they are taken to the 'Get Started' screen
  * Verified that when the user presses '2' and 'Enter' they are taken to the rules screen

### Rules Screen

  * Verified that the console screen clears and the Rules screen has loaded.
  * Verified that the rules scroll up as intended until it asks for user input
  * Verified that the user validation works as intended
  * Verified that when the user presses 'c' or 'C' and 'Enter', they are taken to the second part of the Rules screen which is a navigation menu
  * Verified that the user validation for the menu works correctly
  * Verified that when the user presses '1' and 'Enter' they are returned to the Welcome Screen
  * Verified that when the user presses '2' and 'Enter they move on to the 'Get Started' screen

### Get Started Screen - Create Username/Player Login

  * Verified that the Player 1 menu is called first.
  * Verified that input validation works as intended.
  * Verified that if the user presses '1' and 'Enter' they are take to the Create Username Screen
    * Verified that the user input validation works as intended. See [Username Testing](<#username-testing>)
    * Verified that once the user creates their username, they are greeted on screen by their usernam and that the username was added to the Google Sheets worksheet
    * Verified that the correct data(0 for Total Wins and 0 for Total Losses) was set for the new user in Google Sheets
    * Verified that once the username passes validation, Player 2's menu screen loads
  * Verified that if the user presses '2' and Enter they are taken to the Login Screen
    * Verified that the user input validation works as insteded. See [Username Testing](<#username-testing>)
    * Verified that once the user logins, they are greeted on screen y their username and that the relevant data history for the user that logged in has been correctly retrieved.
    * Verified that once the username login passes validation, Player 2's menu screen loads.
  * Verified that all the above steps also apply to the player 2 login
  * Verified that a combination of Player 1 Create Username, Player 2 Create Username; Player 1 Create Username, Player 2 Login; Player 1 Login, Player 2 Create Username; Player 1 Login, Player 2 Login, all work seamlessing, no matter what combination you try and that the appropriate data is pulled for each isntance of the user.

### Start Screen

  * Verified that both players are asked by their usernames if they are ready
  * Verified that 'Press 'C' to continue input is called.
  * Verified that input validation works as intended. See [Press C to Continue](<#press-c-to-continue>)
  * Verified that if the user presses 'C' a 3 secound countdown is initiated on screen
  * Verified that upon finish of the countdown, the console is cleared and that 'Play' appears on the screen
  * Verified that the Game Screen loads after the above

### Game Screen

  * Verified that the Game Bar is called first, with the gameboard secound and user input third.
  * Verified that the information called in the Game Bar is correct; that the current game stats are set to all 0 for both players and that the History/Overall Stats match the information saved in the Google Sheets
  * Verified that Player 1 is called first to make their move
  * Verified that input validation works correctly. See [Game Validation](<#game-validation>)
  * Verified that once the player one makes their move:
    1. The player piece drops in the appropriate column, matching the users input value
    2. That the player pieces match the player correectly (Red for player 1 and yellow for Player 2)
    3. That if the column is full the player cannot place their piece there.
    4. That player 2 is called after player 1 in a seamless loop until the game ends.
  * Verified that the game can be won if 4 pieces are matched horizontally in a row of one color
  * Verified that the game can be won if 4 pieces are matched vertically in a row of one color
  * Verified that the game can be won if 4 pieces are matched diagonally in a row of one color(both ways)
  * Verified that the game can end in a tie if no 4 in a row matched are made
  * Verified that once the win is made the appropriate player is congratulated by name as the winner and that the scores are immediately updated, both on screen and in Google Sheets
  * Verified that if there is no winner, that the appropriate message appears on the screen and the scores are not updated
  * Verified that once the game ends, the players cannot place any more pieces on the board and that the user input appears ('Press C to continue)
  * Verified that input validation works as intended. See [Press c to continue](<#press-c-to-continue>)
  * Verified that after the user presses 'C' they are taken to the Play Again screen

### Play Again Screen

  * Verified that the Play Again menu loads.
  * Verified that all input validation works correctly. See [Menu Items](<#menu-items>)
  * Verified that if the user press '1':
    1. That the users is taken to a loading screen, telling the players a new game is started and both players are called by their usernames on screen
    2. That after the loading screen the users are taken straight to the Start Screen
    3. That after playing the game from there, that things like the player username and scores are all correct, and continued from the last game.
    4. That the game loops seemlessly as they users play back to the Play Again screen
  * Verified that if the user presses '2':
    1. That the users are taken back to the Welcome Screen
    2. That if they play from there (create username or logging in again), that the user data is reset appropriately i.e. Current game stats are reset, total overal stats are pulled correctly and relevant to whatever users logged in/created a username.
    3. That the game plays seemlessly in a loop
  * Verified that if the user presses '3':
    1. That the users are taken to the High Scores screen
  * Verified that if the user presses '4':
    1. That the users are taken to the exit screen

### High Scores Screen

  * Verified that the High Scores screen load
  * Verified that the current user stats are displayed in a Game Bar (same as that in the Game Screen)
  * Verified that the leaderboard data displays the top 5 scores, sorted by number of wins in descending order and that it matcges the data in Google Sheets
  * Verified that all input validation works as intended. See [Press C to Continue](<#press-c-to-continue>)
  * Verified that if the user presses 'C' they are brought back to the Play Again screen
  
### Exit Screen

  * Verified that the Exit screen loads
  * Verified that a goodbye message appears on the screen for the users.
  * Verified that the program quits

### Other

  * Verified that all data being pushed and pulled from Google Sheets is correct; Usernames, total wins and total losses
  * Verified that the game plays seemlessly in a loop regardless of which option is chosen in the Play Again screen

</details>

[Back to top](<#contents>)  

## Validation

<details><summary>Validation Info </summary>

### Username Testing

The username should between 3 and 10 characters. A username consisting of just blank spaces is not allowed and blank spaces at the beginning and end of username inputs are removed. A username already stored in the system is not allowed.

In the username section:

* Press the 'Enter' key without input and the following is returned:

  * A red string reports the error to the user.
  * The input is initiated again

  ![Error for hitting Enter without input](docs/images/input-error-handling-blank.png)

* Press 'spacebar' key multiple times creating a blank username and the following is returned:

  * A red string reports the error to the user
  * The in put is initiated again

  ![Error for hitting Enter without input](docs/images/input-error-handling-blank.png)

* Enter a two character username and the following is returned:

  * A red string reports the error to the user
  * The input is initiated again

  ![Username with less than 3 characters](docs/images/input-error-handling-specific-length.png)

* Enter a string greater than 10 characters and the following is returned:

  * A red string reports the error to the user
  * The input is initiated again

  ![Username with less than 3 characters](docs/images/input-error-handling-specific-length.png)

* Enter a username that is already saved in Google Sheets and the following is returned:

  * A red string reports the error to the user
  * The input is initiated again

  ![Username not available](docs/images/input-error-handling-username-taken.png)

* For Player 2 login - Enter a username that is already logged in (Player 1) and the following is returned:

  * A red string reports the error to the user
  * The input is initiated again

  ![Player already logged in](docs/images/cannot-log-in.png)

* Enter a string between 3 and 10 characters and the following is returned:

  * A string in the color of the player (player 1 red and player 2 yellow) greeting the player
  * Progression to the next screen

  ![Player successfully validates create username](docs/images/create_username_success.png)
  ![Player successfully validates login](docs/images/player2-success-login.png)

### Press 'C' to continue

Press 'C' to continue accepts both small 'c' and capital 'C'. It cannot be any other key, letter or number. It cannot be blank.

* Enter any character other than 'c' or 'C':

  * A red string reports the error to the user
  * The input is initiated again

  ![Error handling for press c to continue](docs/images/error-handling-continue.png)

* Enter a blank space and the following is returned:

  * A string reports the error to the user
  * The input is initiated again

  ![Error handling for press c to continue](docs/images/error-handling-continue.png)

* Enter the 'c' or 'C' key and the users move onto the next screen

### Menu Items

Press 1) to do something, Press 2) to do something else ... Depending on the number of items in the menu, the user could be asked to press '1' or '2' and for the Play Again screen, '1', '2', '3' or '4'. The input does not accept any other character including blank spaces.

* Enter any key other than '1', '2', '3' or '4' and the following is returned:
  
  * A string reports the error to the user
  * The input is initiated again

  ![Menu error handling numeric choices](docs/images/menu-error-handling.png)
  ![Menu error handling numeric choices](docs/images/error-handling-play-again.png)

* Enter the keys '1', '2', '3' or '4' and the following is returned and the user is taken to the relevant screen depending on their choice.

### Game Validation

During the game, the input only accepts numbers between 1 and 10 (representing the columns on the board). It doesn't accept any other letters or numbers or blank spaces. When a column is full, the user cannot pick that column anymore. 

* Enter a letter and the following is return:

  * A red string reports the error to the user#
  * The input is initiated again

  ![Using a letter instead of number](docs/images/letter-input.png)

* Enter a number other than those between and including 1 and 10 and the following is returned:

  * A res string reports the error to the user
  * The input is initiated again

  ![Using an invalid number](docs/images/not-valid-number.png)

* Enter the number of a column which is full and the following is returned:

  * A red string reports the error to the user
  * The input is initiated again

![Entering the column number thats full](docs/images/column-full-error.png)

</details>

[Back to top](<#contents>)

## Bugs Fixed

<details><summary>Bugs Fixed info</summary>

### Adding Data to Google Sheets via Gspread

When initially adding users to Google sheets using the append_row method, there was an invalid data values. Upon research on the use of gspread, it was realised that the data that was being appending was not in a list format. To remedy this, the .split() was used initially.
![Google spread error](docs/images/convert-to-list.png)
But later, that was changed to where the list was added directly in the append_rows statement and as the code was being refactored to make it more efficient by setting the data values of the other two columns at the same time rather than in a different statement.
![Fixed using split method](docs/images/convert-to-list2.png)
![Refactored more efficient code](docs/images/create-list-gspread.png)

### Logic Error When Dealing with Two Usernames

A logic error occured when the creation of the usernames weas initially coded. It occured when Player 1 creates a new username or logs in, it allowed Player 2 to log in with the same username.

![Double player login](docs/images/double-login-bug.png)

To fix this, Player 2's username input had an additional comparison element to it, comparing it to Player 1 ... and if true, it would report an error to the user that the username was already logged in ... and if false it would allow Player 2 to log in.
[Back to top](<#contents>)

![Double player login fix](docs/images/double-login-bug.png)

### Blank Space in Username & Blank Username

User create name and login seemed to be working well, however an error was found when the user entered any blank spaces in their username, whether this was at the beginning of the input or a 2 or 3 word input or just blank spaces for the username.

![Error returned if username is all blank spaces](docs/images/blank-space-username-error.png)

To fix this, the .replace(' ', '') function was used to replace all the white space with a string without any. A string was also added to let the user know when creating their username, that any blank space would be removed from the username.

![Blank space in username bug](docs/images/blank-space-fix.png)
![String added to let user know blank spaces would be removed](docs/images/user-string-added.png)

To catch the username adding just blank spaces as a username, another comparison was added to the validate_player_name function which checks the users input string length and if it is equal to 0 (blank space) then it would return an error to user and reinitiate the input.

![Code fix for checking if the user input is blank](docs/images/blank_space_username-fix.png)
![If a user tries to use blank spaces as a username](docs/images/blank-username-fix.png)

</details>

[Back to top](<#contents>)


## Terminal Compatibility

This project is intended to be used and deployed via Heroku, and the terminal template given to us. Therefore this project was created with that fact in mind. It is not recommended to use this project on a local terminal as certain display positioning would be off, even if the functionality of the game would still be working.

![Heroku Terminal](docs/images/heroku-terminal.png)
![Local Terminal](docs/images/local-terminal.png)

[Back to top](<#contents>)

# Deployment

## Deployment to Heroku

* Log into Heroku (create an account if necessary)
* Click the button called 'New' from the dashboard, underneath the header in the top right corner.
* Pick the 'Create new app' option
* Enter your application name - this name has to be unique - select your region and then click 'Create App'
* This will bring you to your project page. From here, click the 'Settings' tab and scroll down to Config Vars.
* In the KEY input field, enter 'PORT' and in the VALUE input field, enter '8000'.
* Click the 'Add' button to the right to add the Convig Vars.
* On the same page scroll down to the buildpacks section and click 'Add Buildpack'
* Add both the Python and node.js buildpacks but make sure that the **Python buildpack is above the node.js one**
* Go back to the tabs at the top of the page and this time select the 'Deploy' tab.
* Select Github deployment method.
* Search for your repository name and click the 'Connect' button to link your chosen repository
* At the bottom of that page, select your preferred deplyment type; Automatic Deployment or Manual Deployment and wait a few minutes for your project to be deployed.

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

</details>

[Back to top](<#contents>)

# Credits

* [Emoji Unicodes](https://unicode.org/emoji/charts/emoji-list.html)
* [Python tutorial for Connect4 game](https://www.askpython.com/python/examples/connect-four-game) - helped figure out the logic for the game, particularly for the winning moves
* [Exiting a Python Program](https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/) - helped to figure out the best way to do this
* [Figlet fonts sample](http://www.jave.de/figlet/fonts/overview.html)
* [How to structure long strings](https://note.nkmk.me/en/python-long-string/)
* [Try & Except](https://www.w3schools.com/python/python_try_except.asp) - Helped me understand the concept of try and except
* [.replace()](https://www.journaldev.com/23763/python-remove-spaces-from-string) - Used to fix the bug in the username creation

[Back to top](<#contents>)

# Acknowledgements

This program, Connect4 CLI Game was designed and developed in conjunction with the Full Stack Software Developer Diploma course (eccommerce) at the Code Institute. I would like to thank my mentor, my cohort facilitator, the members of our cohort, the Slack community and Code Institute for all their support.

[Back to top](<#contents>)
