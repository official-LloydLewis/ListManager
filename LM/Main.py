import os
import time
import colorama
import subprocess
from Others.Loadings import Loading



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

        print(WHITE + BOLD + """   
            [1] add USER
            [2] remove USER
            [3] show all USERS
            [4] help guide
            [q] exit
            """ + RESET)

def main():
    error_count = 0
    max_errors = 3
    while True:
        Title.Clear_Title()
        
        # Get user input
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            Title.Clear_Title()
            Loading.display_loading()
            time.sleep(1)  # Brief pause before loading
            try:
                # Run add.py script
                subprocess.run(['python', 'C:\\Users\\Asus\\Documents\\GitHub\\ListManager-Plugin\\LM\\ListManager\\add.py'], check=True)
            except subprocess.CalledProcessError as e:
                print(RED + BOLD + f"Error occurred: {e}" + RESET)
            error_count = 0

        elif choice == '2':
            Title.Clear_Title()
            Loading.display_loading()
            time.sleep(1)  # Brief pause before loading
            try:
                # Run add.py script
                subprocess.run(['python', 'C:\\Users\\Asus\\Documents\\GitHub\\ListManager-Plugin\\LM\\ListManager\\help.py'], check=True)
            except subprocess.CalledProcessError as e:
                print(RED + BOLD + f"Error occurred: {e}" + RESET)
            error_count = 0

        elif choice == '3':
            Title.Clear_Title()
            print("Showing all users... (this is just a placeholder)")
            error_count = 0
            
        elif choice == '4':
            Title.Clear_Title()
            Loading.display_loading()
            time.sleep(1)  # Brief pause before loading
            try:
                # Run add.py script
                subprocess.run(['python', 'C:\\Users\\Asus\\Documents\\GitHub\\ListManager-Plugin\\LM\\ListManager\\help.py'], check=True)
            except subprocess.CalledProcessError as e:
                print(RED + BOLD + f"Error occurred: {e}" + RESET)
            error_count = 0

        elif choice.lower() == 'q':
            print("Exiting...")
            break
        else:
            print(WHITE + "-----------------------------------------------" + RESET)
            print(RED + BOLD + "Invalid choice. Please try again." + RESET)
            print(WHITE + "-----------------------------------------------" + RESET)
            error_count += 1
        
        if error_count >= max_errors:
            time.sleep(3)
            Cls.clear()
            error_count = 0
        else:
            time.sleep(2)  # Pause before clearing the screen for any choice
        
if __name__ == "__main__":
    main()
