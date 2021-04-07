from colorama import init, deinit
from colorama import Fore, Back, Style

fore_back_mapping = {
    'RED_ON_WHITE': Fore.RED + Back.WHITE,
    'GREEN_ON_WHITE': Fore.GREEN + Back.WHITE,
    'BLUE_ON_WHITE': Fore.BLUE + Back.WHITE,
    'MAGENTA_ON_WHITE': Fore.MAGENTA + Back.WHITE,
    'BLACK_ON_WHITE': Fore.BLACK + Back.WHITE,

    'RED_ON_YELLOW': Fore.RED + Back.YELLOW,
    'GREEN_ON_YELLOW': Fore.GREEN + Back.YELLOW,
    'BLUE_ON_YELLOW': Fore.BLUE + Back.YELLOW,
    'MAGENTA_ON_YELLOW': Fore.MAGENTA + Back.YELLOW,
    'BLACK_ON_YELLOW': Fore.BLACK + Back.YELLOW,

    # separations
    'RED_ON_RED': Fore.RED + Back.RED,

}



def colorify(text, fore='GREEN', back='WHITE', highlight=''):
    color = fore_back_mapping.get(fore + '_ON_' + back, None)
    if not color:
        print(text)
    
    if highlight:
        init()
        print()
        print(color + '\t\t=========>'+ highlight , end='\n\n')
    else:
        init(autoreset=True)
    print(color + str(text) + Style.RESET_ALL)
    #deinit()