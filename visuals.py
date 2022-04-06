from pyfiglet import figlet_format


def blank_line():
    """
    Function to print off a blank line
    """
    print(' ')

def connect4_title():
    """
    Function to print off the connect 4 title
    """
    print(figlet_format(' Connect 4!', font = "banner"))