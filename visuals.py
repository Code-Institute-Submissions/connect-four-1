import sys
import time
from colorama import init
from pyfiglet import figlet_format
from termcolor import cprint
import run
import validation as val

init(autoreset=True)


def blank_line():
    """
    Function to print off a blank line
    """
    print(' ')


def connect4_title():
    """
    Function to print off the connect 4 title
    """
    color = 'yellow'
    cprint(figlet_format(' Connect            4 !          ',
                         font="banner3-D",
                         justify='center'),
           color,
           attrs=['bold'])


def game_bar():
    """
    Function which creates a game bar displaying player info
    Using cprint statements
    """
    cprint(' '.center(80), run.COLORS['WHITE'], run.COLORS['BLUE_HL'])
    cprint(
        f"{val.player1_name} - wins: {val.player1_wins}  "
        f"Losses: {val.player1_losses}      "
        f"{val.player2_name} - wins: {val.player2_wins} "
        f"Losses: {val.player2_losses}".center(80), run.COLORS['WHITE'],
        run.COLORS['BLUE_HL'])
    cprint(
        f" History - wins: {val.player1_total_wins} "
        f"Losses: {val.player1_total_losses}    "
        f"History - wins: {val.player2_total_wins}  "
        f"Losses: {val.player2_total_losses}".center(80), run.COLORS['WHITE'],
        run.COLORS['BLUE_HL'])
    cprint(' '.center(80), run.COLORS['WHITE'], run.COLORS['BLUE_HL'])


def game_over_text(player):
    """
    Function which creates a game-over bar
    Displays the winner of the game
    Takes the player parameter
    """
    if player == 0:
        cprint(' '.center(80), run.COLORS['WHITE'], run.COLORS['RED_HL'])
        cprint(f'PLAYER 1 : {val.player1_name} WINS! '.center(80),
               run.COLORS['WHITE'], run.COLORS['RED_HL'])
        cprint('GAME OVER!'.center(80), run.COLORS['WHITE'],
               run.COLORS['RED_HL'])
        cprint(' '.center(80), run.COLORS['WHITE'], run.COLORS['RED_HL'])
    elif player == 1:
        cprint(' '.center(80), run.COLORS['WHITE'], run.COLORS['YELLOW_HL'])
        cprint(f'PLAYER 2 : {val.player2_name} WINS! '.center(80),
               run.COLORS['WHITE'], run.COLORS['YELLOW_HL'])
        cprint('GAME OVER!'.center(80), run.COLORS['WHITE'],
               run.COLORS['YELLOW_HL'])
        cprint(' '.center(80), run.COLORS['WHITE'], run.COLORS['YELLOW_HL'])
    else:
        cprint(' '.center(80), run.COLORS['WHITE'], run.COLORS['BLUE_HL'])
        cprint('NO WINNERS! '.center(80), run.COLORS['WHITE'],
               run.COLORS['BLUE_HL'])
        cprint('GAME OVER!'.center(80), run.COLORS['WHITE'],
               run.COLORS['YELLOW_HL'])
        cprint(' '.center(80), run.COLORS['WHITE'], run.COLORS['BLUE_HL'])


def typing_text(text):
    """
    Loops through characters in a string
    Creates the effect pf tiping using sys.stdout
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
