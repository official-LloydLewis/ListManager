import curses
import json
import os
import colorama
import sys
from ConfigLoader import ConfigLoader
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Others.Titels import TITELS

# Initialize colorama
colorama.init()

# Color configurations
WHITE = colorama.Fore.WHITE
BOLD = colorama.Style.BRIGHT
RESET = colorama.Style.RESET_ALL
YELLOW = colorama.Fore.YELLOW
RED = colorama.Fore.RED

def display_title(stdscr):
    """Display the title at the top of the terminal."""
    title = TITELS.display_titel(YELLOW)
    stdscr.addstr(0, 0, title, curses.A_BOLD)  # Print title at the top-left corner
    stdscr.refresh()

def load_users():
    """Load users from the JSON file."""
    users_file_path = os.path.join(os.path.dirname(__file__), '..', 'Database', 'USERS.json')

    if not os.path.isfile(users_file_path):
        raise FileNotFoundError(f"Users file not found: {users_file_path}")

    with open(users_file_path, 'r') as file:
        data = json.load(file)
    
    users = [{'code': user_data.get('code', 'N/A'), 'name': user_data.get('name', 'Unknown')} for user_data in data]
    
    return users

def update_user_codes():
    """Renumber user codes to ensure they are sequential."""
    users_file_path = os.path.join(os.path.dirname(__file__), '..', 'Database', 'USERS.json')

    if not os.path.isfile(users_file_path):
        raise FileNotFoundError(f"Users file not found: {users_file_path}")

    with open(users_file_path, 'r') as file:
        data = json.load(file)

    # Renumber codes sequentially
    for index, user in enumerate(data):
        user['code'] = f"{index + 1:03d}"

    # Write updated data back to the file
    with open(users_file_path, 'w') as file:
        json.dump(data, file, indent=4)

def display_users(stdscr, users, selected_idx):
    """Display the list of users with selection highlighting."""
    stdscr.clear()
    
    # Display the title
    display_title(stdscr)

    # Add spacing between title and list
    stdscr.addstr(4, 0, '')  # Add space after the title
    
    # Display the users
    start_y = 8  # Start a few lines below the title
    for idx, user in enumerate(users):
        # Format the user info
        user_str = f"Code: {user['code']} | Name: {user['name']}"

        # Set color based on selection
        if idx == selected_idx:
            stdscr.addstr(start_y + idx, 0, user_str, curses.color_pair(1))  # Highlight selected user
        else:
            stdscr.addstr(start_y + idx, 0, user_str)  # Normal display

    stdscr.refresh()

def remove_user(stdscr):
    """Handle user removal and update user codes."""
    # Initialize curses color pair
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)  # Yellow background for selected item

    try:
        # Load users from file
        users = load_users()

        # Initialize selection index
        selected_idx = 0

        while True:
            display_users(stdscr, users, selected_idx)
            
            key = stdscr.getch()

            if key == ord('q'):  # Quit
                break
            elif key == curses.KEY_DOWN and selected_idx < len(users) - 1:
                selected_idx += 1
            elif key == curses.KEY_UP and selected_idx > 0:
                selected_idx -= 1
            elif key == ord('\n'):  # Enter key
                if users:
                    # Remove the selected user
                    del users[selected_idx]
                    # Save updated users to the file
                    users_file_path = os.path.join(os.path.dirname(__file__), '..', 'Database', 'USERS.json')
                    with open(users_file_path, 'w') as file:
                        json.dump(users, file, indent=4)
                    # Update user codes
                    update_user_codes()
                    # Update the display
                    stdscr.clear()
                    stdscr.addstr(0, 0, "User deleted successfully!", colorama.Fore.GREEN + colorama.Style.BRIGHT)
                    stdscr.refresh()
                    stdscr.getch()  # Wait for user input before continuing
                else:
                    stdscr.clear()
                    stdscr.addstr(0, 0, "No users to delete.", colorama.Fore.RED + colorama.Style.BRIGHT)
                    stdscr.refresh()
                    stdscr.getch()  # Wait for user input before continuing

    except Exception as e:
        stdscr.clear()
        stdscr.addstr(0, 0, f"Error: {e}", colorama.Fore.RED + colorama.Style.BRIGHT)
        stdscr.refresh()
        stdscr.getch()  # Wait for user input before closing

curses.wrapper(remove_user)
