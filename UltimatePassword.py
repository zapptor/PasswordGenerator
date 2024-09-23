import sys
import re
import secrets
import string
import os
from time import sleep    
from typing import List



UPPERCASE_REGEX = re.compile(r'[A-Z]')
LOWERCASE_REGEX = re.compile(r'[a-z]')
DIGIT_REGEX = re.compile(r'[0-9]')
SPECIAL_CHAR_REGEX = re.compile(r'[!@#$%^&*()_+{}:;<>,.?~]')


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def strong_password_check_list(passwords: List[str]) -> List[str]:
    """
    Returns a list of passwords that meet the strength criteria.
    """
    
    accepted_passwords = []
    for password in passwords:
        if strong_passwd_check(password):   
            accepted_passwords.append(password)
    return accepted_passwords


def strong_passwd_check(password) -> bool:
    '''
    Check if a password is strong
    
    '''
    return (
        len(password) >= 8 and
        UPPERCASE_REGEX.search(password) and
        LOWERCASE_REGEX.search(password) and
        DIGIT_REGEX.search(password) and
        SPECIAL_CHAR_REGEX.search(password)
        )

    
def password_generator(password_length: int = None, existing_password: str = None) -> str:
    """
    Generates strong password, If existing password is provided, it appends
    random characters to strenghten it, until it meets the criteria.
    
    """
    alphabet = string.ascii_letters + string.digits + string.punctuation
    if existing_password:
        while not strong_passwd_check(existing_password):
            existing_password += secrets.choice(alphabet)
        return existing_password
    elif password_length:
        while True:
            password = ''.join(secrets.choice(alphabet) for _ in range(password_length))
            if strong_passwd_check(password):
                return password
    

def password_substitute(password: str) -> str:
    '''
    takes a password and substitute the character
    to make it stronger
    
    '''

    password_substitut_characters = {
    "a": ["@", "A", "4"],
    "b": ["8", "B", "|3", "6"],
    "c": ["<", "C", "("],
    "d": ["D", "|)", "[)"],
    "e": ["3", "E", "&"],
    "f": ["F", "|="],
    "g": ["9", "G", "6", "q"],
    "h": ["#", "H", "|-|"],
    "i": ["1", "I", "!", "|", "l"],
    "j": ["J", "]"],
    "k": ["K", "|<", "|{"],
    "l": ["1", "|", "£"],
    "m": ["M", "|\/|"],
    "n": ["N", "^"],
    "o": ["0", "O", "()"],
    "p": ["P", "|D"],
    "q": ["Q", "9"],
    "r": ["R", "2"],
    "s": ["5", "S", "$", "§", "z"],
    "t": ["7", "T", "+"],
    "u": ["U", "|_|"],
    "v": ["V", "\/"],
    "w": ["W", "\/\/"],
    "x": ["X", "%", "*"],
    "y": ["Y", "`/"],
    "z": ["2", "Z", "7_"]
    }
    substitute_password = ""
    for letter in password:
        if letter in password_substitut_characters:
            substitute_password += secrets.choice(password_substitut_characters[letter])
        else:
            substitute_password += letter
    return substitute_password


def password_generator_menu():
    while True:
        clear_screen()
        user_input = input("\nPassword Generation\nEnter length of password or 'b' to go back: ")
        if user_input.lower() == "b":
            return
        elif user_input.isdigit():
            password_length = int(user_input)
            if password_length < 10:
                print("Password length below 10 is not recommended. Please enter a length of 10 or more.")
                sleep(1)
                continue
            random_password = password_generator(password_length)
            print(f'\nGenerated Password: {random_password}\n')
        else:
            print("Invalid input. Please enter a numeric value.")
        input("Press Enter to continue...")


def strong_passwd_check_menu():
    while True:
        clear_screen()
        user_input = input("\nCheck Password Strenght\nEnter Password or 'b' to go back: ")
        sleep(0.5)
        if user_input == 'b':
            clear_screen()
            return
        elif strong_passwd_check(user_input): 
            print("\nSTRONG PASSWORD")
            input("\nPress Enter to continue...")
        else:
            print("\nWEAK PASSWORD")            
            input("\nPress Enter to continue...")


def strong_password_check_list_menu():
    while True:
        clear_screen()
        user_input = input("\nCheck list of passwords\ninput the password list (1, 2, 3) or 'b' to go back: ")
        sleep(1)
        if user_input.lower() == 'b':
            clear_screen()
            return
        else:
            passwords = user_input.split(", ")
            strong_password_list = (strong_password_check_list(passwords))
            print(f'\nList of safe passwords:\n{", ".join(strong_password_list)}\n')
            sleep(1)
            input("Press Enter to continue...")
            clear_screen()


def password_substitute_menu():
    while True:
        clear_screen()
        user_input = input("\nPassword Substitute Characters\nInput the password or 'b' to go back: ")
        sleep(1)
        if user_input.lower() == 'b':
            clear_screen()
            return
        else:
            password_sub = (password_substitute(user_input))
            if strong_passwd_check(password_sub):
                print(f'Password Substitute: {password_sub}\n')
                input("Press Enter to continue...")
                clear_screen()
            else:
                print(f'Password isnt strong\n')
                sleep(1)
                print(f'Here Is a Strong Password: {password_generator(existing_password=password_sub)}')
                input("\nPress Enter to continue...")


def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Generate Random Password")
        print("2. Check Password Strength")
        print("3. Check List of Passwords")
        print("4. Password Substitute Characters")
        print("Q. Quit")
        choice = input("Choose an option: ").strip().lower()
        if choice == "q":
            clear_screen()
            sys.exit("Exiting program...")
        elif choice == "1":
            password_generator_menu()
        elif choice == "2":
            strong_passwd_check_menu()
        elif choice == "3":
            strong_password_check_list_menu()
        elif choice == "4":
            password_substitute_menu()
        else:
            print("Invalid choice. Please try again.")


def main():
    clear_screen()
    main_menu()


if __name__ == "__main__":
    main()
