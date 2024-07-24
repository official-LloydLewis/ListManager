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
    def Clear_Title():
        Cls.clear()
        print(YELLOW + BOLD +"""
         _      _     _                                                  
        | |    (_)   | | Best list manager plugin!                                                
        | |     _ ___| |_   _ __ ___   __ _ _ __   __ _  __ _  ___ _ __  
        | |    | / __| __| | '_ ` _ \ / _` | '_ \ / _` |/ _` |/ _ \ '__| 
        | |____| \__ \ |_  | | | | | | (_| | | | | (_| | (_| |  __/ |    
        |______|_|___/\__| |_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_|    
                                                        __/  |           
                                                       |____/   by: LloydLewizzz          
        """+ RESET)

        print(WHITE + BOLD+"""   
            [1] add USER
            [2] remove USER
            [3] show all USERS
            [4] help guide
            [q] exit
            """+ RESET)

def main():
    max_errors = 3  # Maximum number of errors before clearing the screen
    error_count = 0
    
    while True:
        Title.Clear_Title()
        choice = input(BOLD + GREEN + "Enter your choice: " + RESET + WHITE).strip()
        
        if choice == '1':
            # Placeholder for add user functionality
            print(BOLD + GREEN + "Add user selected." + RESET)
            error_count = 0  # Reset error count on valid input
        elif choice == '2':
            # Placeholder for remove user functionality
            print(BOLD + GREEN + "Remove user selected." + RESET)
            error_count = 0  # Reset error count on valid input
        elif choice == '3':
            # Placeholder for show all users functionality
            print(BOLD + GREEN + "Show all users selected." + RESET)
            error_count = 0  # Reset error count on valid input
        elif choice == '4':
            # Placeholder for help guide functionality
            print(BOLD + GREEN + "Help guide selected." + RESET)
            error_count = 0  # Reset error count on valid input
        elif choice.lower() == 'q':
            break
        else:
            error_count += 1
            print(WHITE + "-----------------------------------------------" + RESET)
            print(RED + BOLD + "Invalid choice. Please try again." + RESET)
            print(WHITE + "-----------------------------------------------" + RESET)
            if error_count >= max_errors:
                time.sleep(3)  # Wait for 3 seconds before clearing the screen
                Cls.clear()
                error_count = 0  # Reset error count after clearing the screen

if __name__ == "__main__":
    main()
