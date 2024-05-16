
color_codes = {
    "BLACK": "\033[30m",
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "MAGENTA": "\033[35m",
    "CYAN": "\033[36m",
    "WHITE": "\033[37m",

    "LIGHTBLACK": "\033[90m",
    "LIGHTRED": "\033[91m",
    "LIGHTGREEN": "\033[92m",
    "LIGHTYELLOW": "\033[93m",
    "LIGHTBLUE": "\033[94m",
    "LIGHTMAGENTA": "\033[95m",
    "LIGHTCYAN": "\033[96m",
    "LIGHTWHITE": "\033[97m",

    "BOLD": "\033[1m",
    "UNDERLINE": "\033[4m",

    "BACKGROUND_BLACK": "\033[40m",
    "BACKGROUND_RED": "\033[41m",
    "BACKGROUND_GREEN": "\033[42m",
    "BACKGROUND_YELLOW": "\033[43m",
    "BACKGROUND_BLUE": "\033[44m",
    "BACKGROUND_MAGENTA": "\033[45m",
    "BACKGROUND_CYAN": "\033[46m",
    "BACKGROUND_WHITE": "\033[47m",

    "LIGHTBACKGROUND_BLACK": "\033[100m",
    "LIGHTBACKGROUND_RED": "\033[101m",
    "LIGHTBACKGROUND_GREEN": "\033[102m",
    "LIGHTBACKGROUND_YELLOW": "\033[103m",
    "LIGHTBACKGROUND_BLUE": "\033[104m",
    "LIGHTBACKGROUND_MAGENTA": "\033[105m",
    "LIGHTBACKGROUND_CYAN": "\033[106m",
    "LIGHTBACKGROUND_WHITE": "\033[107m",

    "RESET": "\033[0m"
}  


def Black(string):
    return f"{color_codes['BLACK']}{string}{color_codes['RESET']}"

def Red(string):
    return f"{color_codes['RED']}{string}{color_codes['RESET']}"

def Green(string):
    return f"{color_codes['GREEN']}{string}{color_codes['RESET']}"

def Yellow( string):
    return f"{color_codes['YELLOW']}{string}{color_codes['RESET']}"

def Blue(string):
    return f"{color_codes['BLUE']}{string}{color_codes['RESET']}"

def Magenta(string):
    return f"{color_codes['MAGENTA']}{string}{color_codes['RESET']}"

def Cyan(string):
    return f"{color_codes['CYAN']}{string}{color_codes['RESET']}"

def White(string):
    return f"{color_codes['WHITE']}{string}{color_codes['RESET']}"

def LightBlack(string):
    return f"{color_codes['LIGHTBLACK']}{string}{color_codes['RESET']}"

def LightRed(string):
    return f"{color_codes['LIGHTRED']}{string}{color_codes['RESET']}"

def LightGreen(string):
    return f"{color_codes['LIGHTGREEN']}{string}{color_codes['RESET']}"

def LightYellow(string):
    return f"{color_codes['LIGHTYELLOW']}{string}{color_codes['RESET']}"

def LightBlue(string):
    return f"{color_codes['LIGHTBLUE']}{string}{color_codes['RESET']}"

def LightMagenta(string):
    return f"{color_codes['LIGHTMAGENTA']}{string}{color_codes['RESET']}"

def LightCyan(string):
    return f"{color_codes['LIGHTCYAN']}{string}{color_codes['RESET']}"

def LightWhite(string):
    return f"{color_codes['LIGHTWHITE']}{string}{color_codes['RESET']}"

def Bold(string):
    return f"{color_codes['BOLD']}{string}{color_codes['RESET']}"

def Underline(string):
    return f"{color_codes['UNDERLINE']}{string}{color_codes['RESET']}"

def BackgroundBlack(string):
    return f"{color_codes['BACKGROUND_BLACK']}{string}{color_codes['RESET']}"

def BackgroundRed(string):
    return f"{color_codes['BACKGROUND_RED']}{string}{color_codes['RESET']}"

def BackgroundGreen(string):
    return f"{color_codes['BACKGROUND_GREEN']}{string}{color_codes['RESET']}"

def BackgroundYellow(string):
    return f"{color_codes['BACKGROUND_YELLOW']}{string}{color_codes['RESET']}"

def BackgroundBlue(string):
    return f"{color_codes['BACKGROUND_BLUE']}{string}{color_codes['RESET']}"

def BackgroundMagenta(string):
    return f"{color_codes['BACKGROUND_MAGENTA']}{string}{color_codes['RESET']}"

def BackgroundCyan(string):
    return f"{color_codes['BACKGROUND_CYAN']}{string}{color_codes['RESET']}"

def BackgroundWhite(string):
    return f"{color_codes['BACKGROUND_WHITE']}{string}{color_codes['RESET']}"

def LightBackgroundBlack(string):
    return f"{color_codes['LIGHTBACKGROUND_BLACK']}{string}{color_codes['RESET']}"

def LightBackgroundRed(string):
    return f"{color_codes['LIGHTBACKGROUND_RED']}{string}{color_codes['RESET']}"

def LightBackgroundGreen(string):
    return f"{color_codes['LIGHTBACKGROUND_GREEN']}{string}{color_codes['RESET']}"

def LightBackgroundYellow(string):
    return f"{color_codes['LIGHTBACKGROUND_YELLOW']}{string}{color_codes['RESET']}"

def LightBackgroundBlue(string):
    return f"{color_codes['LIGHTBACKGROUND_BLUE']}{string}{color_codes['RESET']}"

def LightBackgroundMagenta(string):
    return f"{color_codes['LIGHTBACKGROUND_MAGENTA']}{string}{color_codes['RESET']}"

def LightBackgroundCyan(string):
    return f"{color_codes['LIGHTBACKGROUND_CYAN']}{string}{color_codes['RESET']}"

def LightBackgroundWhite(string):
    return f"{color_codes['LIGHTBACKGROUND_WHITE']}{string}{color_codes['RESET']}"


def main():
    # Now you can use the terminal_color object to call methods
    print(Green("This text will be green."))

if __name__ == "__main__":
    main()  