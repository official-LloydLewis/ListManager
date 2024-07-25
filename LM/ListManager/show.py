import json
import os
from ConfigLoader import config_loader
from USERS import USERS
import colorama
import time

# Initialize colorama
colorama.init()

# Color configurations
RED = colorama.Fore.RED
GREEN = colorama.Fore.GREEN
WHITE = colorama.Fore.WHITE
L_GREEN = colorama.Fore.LIGHTGREEN_EX
BOLD = colorama.Style.BRIGHT
RESET = colorama.Style.RESET_ALL
YELLOW = colorama.Fore.YELLOW

# Clear class
class Cls:
    @staticmethod
    def clear():
        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For Unix-like systems (Linux, macOS)
            os.system('clear')

class Title:
    @staticmethod
    def show_title():
        print(YELLOW + BOLD + """
         _      _     _                                                  
        | |    (_)   | | Best list manager plugin!                                                
        | |     _ ___| |_   _ __ ___   __ _ _ __   __ _  __ _  ___ _ __  
        | |    | / __| __| | '_ ` _ \ / _` | '_ \ / _` |/ _` |/ _ \ '__| 
        | |____| \__ \ |_  | | | | | | (_| | | | | (_| | (_| |  __/ |    
        |______|_|___/\__| |_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_|    
                                                        __/  |           
                                                       |____/   by: LloydLewizzz        
                
        """ + RESET)

def show_list():
    Cls.clear()
    Title.show_title()
    path = config_loader.get_path('data_folder')

    if not os.path.exists(path):
        print(RED + BOLD + "Data file does not exist." + RESET)
        time.sleep(2)
        return

    try:
        with open(path, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print(RED + BOLD + "Error reading JSON file." + RESET)
        time.sleep(2)
        return

    if not data:
        print(RED + BOLD + "No users found." + RESET)
        time.sleep(2)
        return

    for user in data:
        print(f"{WHITE}Code: {user['code']}")
        print(f"Name: {user['name']}")
        print(f"Age: {user['age']}")
        print(f"Gender: {user['gender']}")
        print(f"Active Now: {user['active_now']}")
        print(f"Activity Time: {user['activity_time']}")
        print(f"Role: {user['role']}")
        print(WHITE + "-----------------------------------------------")

    input(BOLD + GREEN + "Press Enter to return to the menu..." + RESET)

if __name__ == "__main__":
    show_list()
