from aws_login import login_to_aws, is_logged_in
from language_selector import select_language
from translator import translate_text
from colorama import Fore, Style, init

init(autoreset=True)

def main_menu():
    print(Fore.CYAN + "DISCLAIMER: You need an AWS account and permission for the Translate service to use this program.")
    
    source_language_code = None
    target_language_code = None
    session = None
    region = None

    while True:
        try:
            select = int(input(Fore.CYAN + "1. Login\n2. Select Language\n3. Translate\n4. Exit\n"))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")
            continue

        if select == 1:
            session, region = login_to_aws()
        elif select == 2:
            if not is_logged_in():
                print(Fore.RED + "You need to log in first.")
            elif session is None or region is None:
                print(Fore.RED + "Region not specified. Please log in again.")
            else:
                source_language_code, target_language_code = select_language(session, region)
        elif select == 3:
            if not is_logged_in():
                print(Fore.RED + "You need to log in first.")
            elif source_language_code is None or target_language_code is None:
                print(Fore.RED + "You need to select the languages first.")
            else:
                translate_text(session, source_language_code, target_language_code)
        elif select == 4:
            print(Fore.GREEN + "Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid selection. Please try again.")

if __name__ == "__main__":
    main_menu()
