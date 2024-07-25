from ConfigLoader import config_loader
from USERS import USERS
import os
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

def input_name():
    while True:
        Cls.clear()
        Title.show_title()
        name = input(BOLD + GREEN + config_loader.get_message('enter_name') + RESET + WHITE)
        if name.isalpha():
            return name
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

def add_user():
    code = USERS.get_next_code()
    if USERS.code_exists(code):
        print(RED + BOLD + config_loader.get_message('code_exists').format(code) + RESET)
        return

    name = input_name()
    age = input_age()
    gender = input_gender()
    role = input_role()

    new_user = USERS(code=code, name=name, age=age, gender=gender, role=role)
    USERS.save_user(new_user)
    print(L_GREEN + BOLD + config_loader.get_message('user_added').format(name, code) + RESET)

# Example usage
if __name__ == "__main__":
    add_user()
