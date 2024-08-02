import colorama

# Initialize colorama
colorama.init()

# Color configurations
WHITE = colorama.Fore.WHITE
BOLD = colorama.Style.BRIGHT
RESET = colorama.Style.RESET_ALL
YELLOW = colorama.Fore.YELLOW

class TITELS:
    @staticmethod
    def display_help_guide(color):
        print(color + """
        /$$   /$$           /$$                                     /$$       /$$          
        | $$  | $$          | $$                                    |__/      | $$          
        | $$  | $$  /$$$$$$ | $$  /$$$$$$         /$$$$$$  /$$   /$$ /$$  /$$$$$$$  /$$$$$$ 
        | $$$$$$$$ /$$__  $$| $$ /$$__  $$       /$$__  $$| $$  | $$| $$ /$$__  $$ /$$__  $$
        | $$__  $$| $$$$$$$$| $$| $$  \ $$      | $$  \ $$| $$  | $$| $$| $$  | $$| $$$$$$$$
        | $$  | $$| $$_____/| $$| $$  | $$      | $$  | $$| $$  | $$| $$| $$  | $$| $$_____/
        | $$  | $$|  $$$$$$$| $$| $$$$$$$/      |  $$$$$$$|  $$$$$$/| $$|  $$$$$$$|  $$$$$$$
        |__/  |__/ \_______/|__/| $$____/        \____  $$ \______/ |__/ \_______/ \_______/
                                | $$             /$$  \ $$                                  
                                | $$            |  $$$$$$/                                  
                                |__/             \______/                                                                                                             
        """ + colorama.Style.RESET_ALL)
        
    @staticmethod
    def display_titel(color):
        return color + """
         _      _     _                                                  
        | |    (_)   | | Best list manager plugin!                                                
        | |     _ ___| |_   _ __ ___   __ _ _ __   __ _  __ _  ___ _ __  
        | |    | / __| __| | '_  _ \ / _ | '_ \ / _ |/ _ |/ _ \ '__| 
        | |____| \__ \ |_  | | | | | | (_| | | | | (_| | (_| |  __/ |    
        |______|_|___/\__| |_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_|    
                                                        __/  |           
                                                       |____/   by: LloydLewizzz 
        """ + colorama.Style.RESET_ALL
