import curses
import json
import os
import sys
import time
import subprocess
import colorama

# Initialize colorama
colorama.init()

# Define paths
base_path = os.path.dirname(__file__)
main_script = os.path.join(base_path, 'LM', 'Main.py')

# Add 'Others' directory to sys.path
sys.path.append(os.path.join(base_path, '..', 'Others'))

# Color configurations
RED = colorama.Fore.RED
GREEN = colorama.Fore.GREEN
WHITE = colorama.Fore.WHITE
L_GREEN = colorama.Fore.LIGHTGREEN_EX
BOLD = colorama.Style.BRIGHT
RESET = colorama.Style.RESET_ALL
YELLOW = colorama.Fore.YELLOW

def load_users():
    users_file_path = os.path.join(base_path, '..', 'Database', 'USERS.json')

    if not os.path.isfile(users_file_path):
        raise FileNotFoundError(f"Users file not found: {users_file_path}")

    with open(users_file_path, 'r') as file:
        data = json.load(file)
    
    return data

def update_user_codes():
    users_file_path = os.path.join(base_path, '..', 'Database', 'USERS.json')

    if not os.path.isfile(users_file_path):
        raise FileNotFoundError(f"Users file not found: {users_file_path}")

    with open(users_file_path, 'r') as file:
        data = json.load(file)

    # Initialize a new list for updated users
    updated_users = []
    used_codes = set()

    # Update codes and collect used codes
    for user in data:
        user_code = user.get('code', None)
        if user_code:
            used_codes.add(user_code)

    # Assign new codes to users, ensuring uniqueness
    code_index = 1
    for user in data:
        user_code = user.get('code', None)
        if not user_code or user_code not in used_codes:
            user['code'] = f"{code_index:03d}"
            code_index += 1
        updated_users.append(user)

    # Save the updated user list to the file
    with open(users_file_path, 'w') as file:
        json.dump(updated_users, file, indent=4)

def display_users(stdscr, users, selected_idx):
    stdscr.clear()
    start_y = 0
    for idx, user in enumerate(users):
        user_str = f"Code: {user['code']} | Name: {user['name']}"
        if idx == selected_idx:
            stdscr.addstr(start_y + idx, 0, user_str, curses.color_pair(1))
        else:
            stdscr.addstr(start_y + idx, 0, user_str)
    stdscr.refresh()

def remove_user(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)

    try:
        users = load_users()
        selected_idx = 0

        while True:
            display_users(stdscr, users, selected_idx)
            
            key = stdscr.getch()

            if key == ord('q'):
                break
            elif key == curses.KEY_DOWN and selected_idx < len(users) - 1:
                selected_idx += 1
            elif key == curses.KEY_UP and selected_idx > 0:
                selected_idx -= 1
            elif key == ord('\n'):
                if users:
                    deleted_user = users.pop(selected_idx)
                    
                    # Save the updated user list to the file
                    users_file_path = os.path.join(base_path, '..', 'Database', 'USERS.json')
                    with open(users_file_path, 'w') as file:
                        json.dump(users, file, indent=4)
                    
                    # Update user codes
                    update_user_codes()
                    
                    stdscr.clear()
                    stdscr.addstr(0, 0, f"REMOVED Code: {deleted_user['code']} | Name: {deleted_user['name']}", curses.color_pair(2) | curses.A_BOLD)
                    stdscr.refresh()
                    
                    time.sleep(5)
                    
                    # Return to main script
                    stdscr.clear()
                    stdscr.addstr(0, 0, "Returning to main script...", curses.color_pair(4) | curses.A_BOLD)
                    stdscr.refresh()
                    time.sleep(2)

                    # Run main.py script
                    try:
                        subprocess.run(['python', main_script], check=True)
                    except subprocess.CalledProcessError as e:
                        stdscr.addstr(0, 0, f"Error occurred: {e}", curses.color_pair(2) | curses.A_BOLD)
                        stdscr.refresh()
                        time.sleep(3)

                    break

                else:
                    stdscr.clear()
                    stdscr.addstr(0, 0, "No users to delete.", curses.color_pair(2) | curses.A_BOLD)
                    stdscr.refresh()
                    stdscr.getch()

    except Exception as e:
        stdscr.clear()
        stdscr.addstr(0, 0, f"Error: {e}", curses.color_pair(2) | curses.A_BOLD)
        stdscr.refresh()
        stdscr.getch()

def main(stdscr):
    remove_user(stdscr)

curses.wrapper(main)
