from colorama import init
from colorama import Fore, Back, Style

fore_back_mapping = {
    'RED_ON_WHITE': Fore.RED + Back.WHITE,
    'GREEN_ON_WHITE': Fore.GREEN + Back.WHITE,
}



def colorify(text, fore='GREEN', back='WHITE'):
    color = fore_back_mapping.get(fore + '_ON_' + back, None)
    if not color:
        print(text)
    init()
    print(color + str(text) + Style.RESET_ALL)