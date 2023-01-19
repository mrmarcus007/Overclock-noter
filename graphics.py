import pyfiglet

def ascii_art(text):
    return pyfiglet.figlet_format(text)

Rever = " \n Overclock Manager, Version: 2.0.1"
Overclock = ascii_art("Overclock Manager")
Menu = ascii_art("Menu")
Warning = ascii_art("Warning")
Bye = ascii_art("Goodbye")