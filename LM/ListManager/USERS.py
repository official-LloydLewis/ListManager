# USERS.py

import json
import os
import colorama
from ConfigLoader import ConfigLoader

# Initialize colorama
colorama.init()

# Color configurations
RED = colorama.Fore.RED
GREEN = colorama.Fore.GREEN
WHITE = colorama.Fore.WHITE
L_GREEN = colorama.Fore.LIGHTGREEN_EX
BOLD = colorama.Style.BRIGHT
RESET = colorama.Style.RESET_ALL

class USERS:
    ROLES = ['owner', 'developer', 'admin', 'member']

    def __init__(self, code, name, age, gender, role):
        self.code = code
        self.name = self.validate_name(name)
        self.age = self.validate_age(age)
        self.gender = self.validate_gender(gender)
        self.active_now = ""
        self.activity_time = ""
        self.role = self.validate_role(role)

    @staticmethod
    def validate_name(name):
        if name.isalpha():
            return name
        else:
            raise ValueError(f"{RED}{BOLD}Name must contain only letters{RESET}")

    @staticmethod
    def validate_age(age):
        if isinstance(age, int) and age > 0:
            return age
        else:
            raise ValueError(f"{RED}{BOLD}Age must be a positive integer{RESET}")

    @staticmethod
    def validate_gender(gender):
        gender = gender.lower()
        if gender in ['male', 'female']:
            return gender
        else:
            raise ValueError(f"{RED}{BOLD}Gender must be 'male' or 'female'{RESET}")

    @staticmethod
    def validate_role(role):
        role = role.lower()
        if role in USERS.ROLES:
            return role
        else:
            raise ValueError(f"{RED}{BOLD}Role must be one of {', '.join(USERS.ROLES)}{RESET}")

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "active_now": self.active_now,
            "activity_time": self.activity_time,
            "role": self.role
        }

    @staticmethod
    def get_next_code():
        config_loader = ConfigLoader(r'C:\Users\Asus\Documents\GitHub\ListManager-Plugin\LM\Config\config.yml')
        path = config_loader.get_path('data_folder')
        if os.path.exists(path):
            try:
                with open(path, 'r') as file:
                    try:
                        data = json.load(file)
                        return f"{len(data) + 1:03d}"
                    except json.JSONDecodeError as e:
                        print(f"{RED}{BOLD}Error reading JSON file: {e}{RESET}")
                        return "001"
            except IOError as e:
                print(f"{RED}{BOLD}IOError: {e}{RESET}")
                return "001"
        else:
            return "001"

    @staticmethod
    def code_exists(code):
        config_loader = ConfigLoader(r'C:\Users\Asus\Documents\GitHub\ListManager-Plugin\LM\Config\config.yml')
        path = config_loader.get_path('data_folder')
        if os.path.exists(path):
            try:
                with open(path, 'r') as file:
                    try:
                        data = json.load(file)
                        return any(user['code'] == code for user in data)
                    except json.JSONDecodeError as e:
                        print(f"{RED}{BOLD}Error reading JSON file: {e}{RESET}")
                        return False
            except IOError as e:
                print(f"{RED}{BOLD}IOError: {e}{RESET}")
                return False
        return False

    @staticmethod
    def save_user(user):
        config_loader = ConfigLoader(r'C:\Users\Asus\Documents\GitHub\ListManager-Plugin\LM\Config\config.yml')
        path = config_loader.get_path('data_folder')
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)  # Create directory if it does not exist

        if os.path.exists(path):
            try:
                with open(path, 'r') as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
            except IOError:
                data = []
        else:
            data = []

        data.append(user.to_dict())

        try:
            with open(path, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"{RED}{BOLD}IOError: {e}{RESET}")

    @staticmethod
    def name_exists(name):
        config_loader = ConfigLoader(r'C:\Users\Asus\Documents\GitHub\ListManager-Plugin\LM\Config\config.yml')
        path = config_loader.get_path('data_folder')
        if os.path.exists(path):
            try:
                with open(path, 'r') as file:
                    try:
                        data = json.load(file)
                        return any(user['name'].lower() == name.lower() for user in data)
                    except json.JSONDecodeError as e:
                        print(f"{RED}{BOLD}Error reading JSON file: {e}{RESET}")
                        return False
            except IOError as e:
                print(f"{RED}{BOLD}IOError: {e}{RESET}")
                return False
        return False
