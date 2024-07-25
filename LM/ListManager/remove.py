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

def remove_user():
    while True:
        Cls.clear()
        Title.show_title()
        code = input(BOLD + GREEN + config_loader.get_message('enter_code') + RESET + WHITE)
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

        user_found = False
        new_data = []

        for user in data:
            if user['code'] == code:
                user_found = True
                print(GREEN + BOLD + f"User with code {code} has been removed." + RESET)
            else:
                new_data.append(user)

        if user_found:
            with open(path, 'w') as file:
                json.dump(new_data, file, indent=4)
            break
        else:
            print(RED + BOLD + "No user found with the given code." + RESET)
            time.sleep(2)

if __name__ == "__main__":
    remove_user()
