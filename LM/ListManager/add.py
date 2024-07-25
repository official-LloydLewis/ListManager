# add.py

from ConfigLoader import ConfigLoader  # Import ConfigLoader class
from USERS import USERS  # Import USERS class
import os
import colorama
import time

# Initialize colorama
colorama.init()

# Load the config
config_loader = ConfigLoader(r'C:\Users\Asus\Documents\GitHub\ListManager-Plugin\LM\Config\config.yml')

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

def input_name():
    while True:
        Cls.clear()
        Title.show_title()
        name = input(BOLD + GREEN + config_loader.get_message('enter_name') + RESET + WHITE)
        if name.isalpha():
            try:
                if USERS.name_exists(name):
                    print(WHITE + "-----------------------------------------------" + RESET)
                    print(RED + BOLD + config_loader.get_message('name_exists_error') + RESET)
                    print(WHITE + "-----------------------------------------------" + RESET)
                    time.sleep(1)
                else:
                    return name
            except ValueError as e:
                print(WHITE + "-----------------------------------------------" + RESET)
                print(str(e))
                print(WHITE + "-----------------------------------------------" + RESET)
                time.sleep(1)
        else:
            print(WHITE + "-----------------------------------------------" + RESET)
            print(RED + BOLD + config_loader.get_message('name_error') + RESET)
            print(WHITE + "-----------------------------------------------" + RESET)
            time.sleep(1)

def input_age():
    while True:
        Cls.clear()
        Title.show_title()
        age = input(BOLD + GREEN + config_loader.get_message('enter_age') + RESET + WHITE)
        if age.isdigit():
            return int(age)
        else:
            print(WHITE + "-----------------------------------------------" + RESET)
            print(RED + BOLD + config_loader.get_message('age_error') + RESET)
            print(WHITE + "-----------------------------------------------" + RESET)
            time.sleep(1)

def input_gender():
    while True:
        Cls.clear()
        Title.show_title()
        gender = input(BOLD + GREEN + config_loader.get_message('enter_gender') + RESET + WHITE).lower()
        if gender in ['male', 'female']:
            return gender
        else:
            print(WHITE + "-----------------------------------------------" + RESET)
            print(RED + BOLD + config_loader.get_message('gender_error') + RESET)
            print(WHITE + "-----------------------------------------------" + RESET)
            time.sleep(1)

def input_role():
    while True:
        Cls.clear()
        Title.show_title()
        role = input(BOLD + GREEN + config_loader.get_message('enter_role') + RESET + WHITE).lower()
        if role in USERS.ROLES:
            return role
        else:
            print(WHITE + "-----------------------------------------------" + RESET)
            print(RED + BOLD + config_loader.get_message('role_error') + RESET)
            print(WHITE + "-----------------------------------------------" + RESET)
            time.sleep(1)

def main():
    Cls.clear()
    Title.show_title()
    name = input_name()
    age = input_age()
    gender = input_gender()
    role = input_role()

    code = USERS.get_next_code()

    try:
        user = USERS(code, name, age, gender, role)
        USERS.save_user(user)
        print(GREEN + BOLD + f"User '{name}' added successfully!" + RESET)
    except ValueError as e:
        print(WHITE + "-----------------------------------------------" + RESET)
        print(str(e))
        print(WHITE + "-----------------------------------------------" + RESET)

if __name__ == "__main__":
    main()
