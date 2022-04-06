from pyfiglet import figlet_format
import colorama
from termcolor import cprint


colorama.init(autoreset=True)


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
    blank_line()
    cprint(figlet_format(' Connect4 !', font = "rev"), color, attrs=['bold'])
    