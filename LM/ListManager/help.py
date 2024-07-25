import sys
import os
from ConfigLoader import ConfigLoader  # Import ConfigLoader class
import colorama
import time
import keyboard  # Import the keyboard module

# اضافه کردن مسیر `ListManager-Plugin\LM` به sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Others.Titels import TITELS  # حالا می‌توانید `TITELS` را وارد کنید

# Initialize colorama
colorama.init()

# Load the config
config_loader = ConfigLoader(r'C:\Users\Asus\Documents\GitHub\ListManager-Plugin\LM\Config\config.yml')

# Color configurations
WHITE = colorama.Fore.WHITE
BOLD = colorama.Style.BRIGHT
RESET = colorama.Style.RESET_ALL
YELLOW = colorama.Fore.YELLOW

def display_help():
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
    import Main
    Main.main()  # Ensure Main.py has a function named `main` to call
