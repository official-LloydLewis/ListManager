import os
import time
import colorama

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

# Loading class
class Loading:
    @staticmethod
    def display_loading():
        ascii_art = {
            "3": RED + BOLD +"""          
             $$$$$$\  
            $$ ___$$\ 
            \_/   $$ |
              $$$$$ / 
              \___$$\ 
            $$\   $$ |
            \$$$$$$  |
             \______/

""" + RESET ,
            "2": RED + BOLD +"""
            $$$$$$\  
            $$  __$$\ 
            \__/  $$ |
            $$$$$$  |
            $$  ____/ 
            $$ |      
            $$$$$$$$\ 
            \________|

""" + RESET ,
            "1": RED + BOLD +"""
              $$\   
            $$$$ |  
            \_$$ |  
              $$ |  
              $$ |  
              $$ |  
           $$$$$$\ 
           \______|

""" + RESET 
        }

        for number in ["3", "2", "1"]:
            Cls.clear()
            print(ascii_art[number])
            time.sleep(1)

# Sample usage of the Loading class
if __name__ == "__main__":
    Loading.display_loading()
