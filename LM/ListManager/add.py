from ConfigLoader import config_loader
from USERS import USERS
import os
import colorama

# Get the new data path
data_path = config_loader.get_path('data_folder')
print(f"Data path: {data_path}")

# Initialize colorama
colorama.init()

# Color configurations
RED = colorama.Fore.RED
GREEN = colorama.Fore.GREEN
WHITE = colorama.Fore.WHITE
L_GREEN = colorama.Fore.LIGHTGREEN_EX
BOLD = colorama.Style.BRIGHT
RESET = colorama.Style.RESET_ALL

# Clear class
class Cls:
    @staticmethod
    def clear():
        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For Unix-like systems (Linux, macOS)
            os.system('clear')

Cls.clear()

def input_name():
    while True:
        name = input(BOLD + GREEN + config_loader.get_message('enter_name') + RESET + WHITE)
        if name.isalpha():
            return name
        else:
            print(WHITE + "-----------------------------------------------" + RESET)
            print(RED + BOLD + config_loader.get_message('name_error') + RESET)
            print(WHITE + "-----------------------------------------------" + RESET)

def input_age():
    while True:
        age = input(BOLD + GREEN + config_loader.get_message('enter_age') + RESET + WHITE)
        if age.isdigit():
            return int(age)
        else:
            print(WHITE + "-----------------------------------------------" + RESET)
            print(RED + BOLD + config_loader.get_message('age_error') + RESET)
            print(WHITE + "-----------------------------------------------" + RESET)

def input_gender():
    while True:
        gender = input(BOLD + GREEN + config_loader.get_message('enter_gender') + RESET + WHITE).lower()
        if gender in ['male', 'female']:
            return gender
        else:
            print(WHITE + "-----------------------------------------------" + RESET)
            print(RED + BOLD + config_loader.get_message('gender_error') + RESET)
            print(WHITE + "-----------------------------------------------" + RESET)

def input_role():
    while True:
        role = input(BOLD + GREEN + config_loader.get_message('enter_role') + RESET + WHITE).lower()
        if role in USERS.ROLES:
            return role
        else:
            print(WHITE + "-----------------------------------------------" + RESET)
            print(RED + BOLD + config_loader.get_message('role_error') + RESET)
            print(WHITE + "-----------------------------------------------" + RESET)

def add_user():
    code = USERS.get_next_code()
    name = input_name()
    age = input_age()
    gender = input_gender()
    role = input_role()

    new_user = USERS(code=code, name=name, age=age, gender=gender, role=role)
    USERS.save_user(new_user)
    print(L_GREEN + BOLD + config_loader.get_message('user_added').format(name, code) + RESET)

if __name__ == "__main__":
    add_user()
