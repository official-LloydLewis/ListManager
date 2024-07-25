import os
import time

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
            "3": """
Loading...
                        
             $$$$$$\  
            $$ ___$$\ 
            \_/   $$ |
              $$$$$ / 
              \___$$\ 
            $$\   $$ |
            \$$$$$$  |
             \______/

            """,
            "2": """
Loading..                      
            $$$$$$\  
            $$  __$$\ 
            \__/  $$ |
            $$$$$$  |
            $$  ____/ 
            $$ |      
            $$$$$$$$\ 
            \________|

            """,
            "1": """
Loading.                     
              $$\   
            $$$$ |  
            \_$$ |  
              $$ |  
              $$ |  
              $$ |  
           $$$$$$\ 
           \______|

            """
        }

        for number in ["3", "2", "1"]:
            Cls.clear()
            print(ascii_art[number])
            time.sleep(1)

# Sample usage of the Loading class
if __name__ == "__main__":
    Loading.display_loading()
