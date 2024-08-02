import sys
import os
import colorama
import time
import keyboard

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ConfigLoader import ConfigLoader  # Import ConfigLoader class
from Others.Titels import TITELS

# Clear class
class Cls:
    @staticmethod
    def clear():
        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For Unix-like systems (Linux, macOS)
            os.system('clear')

# Initialize colorama
colorama.init()

# Define the relative path to the config file
config_path = os.path.join(os.path.dirname(__file__), '..', 'Config', 'config.yml')

# Verify that the config file exists
if not os.path.isfile(config_path):
    raise FileNotFoundError(f"Config file not found: {config_path}")

# Load the config
config_loader = ConfigLoader(config_path)

# Color configurations
WHITE = colorama.Fore.WHITE
BOLD = colorama.Style.BRIGHT
RESET = colorama.Style.RESET_ALL
YELLOW = colorama.Fore.YELLOW

def display_help():
    Cls.clear()
    TITELS.display_help_guide(YELLOW)
    help_guide = config_loader.config.get('help-guide', [])
    max_length = max(len(line) for line in help_guide)
    total_length = max_length + 6  # For padding

    # Add top padding
    print('\n' * 2)

    # Print top border
    print(' ' * ((80 - total_length) // 2) + YELLOW + '=' * total_length + RESET)

    # Print help guide
    for i, line in enumerate(help_guide, start=1):
        padded_line = line.ljust(max_length)
        formatted_line = f"{YELLOW}|{RESET} {WHITE}{BOLD}{i}. {padded_line}{RESET} {YELLOW}|{RESET}"
        print(' ' * ((80 - total_length) // 2) + formatted_line)

    # Print bottom border
    print(' ' * ((80 - total_length) // 2) + YELLOW + '=' * total_length + RESET)

    # Add bottom padding
    print('\n' * 2)

def wait_for_user_input():
    print(WHITE + BOLD + "Press 'q' to return to the main menu" + RESET)
    while True:
        if keyboard.is_pressed('q'):
            break
        time.sleep(0.1)  # Sleep to prevent high CPU usage

if __name__ == "__main__":
    display_help()
    wait_for_user_input()
    
    # Execute the loading animation before returning to the main menu
    from Others.Loadings import Loading
    Loading.display_loading()
    
    # Import and execute the main script
    main_script = os.path.join(os.path.dirname(__file__), '..', 'Main.py')
    if os.path.isfile(main_script):
        import Main
        Main.main()  # Ensure Main.py has a function named `main` to call
    else:
        print(colorama.Fore.RED + "Main.py script not found!" + RESET)
