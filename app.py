from admin import *


def main():
    while True:
        print("********** Welcome to Trivia Game **********")
        print("1. admin")
        print("2. user")
        print("3. exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            check_admin()
        elif choice == 2:
            question_view()
        elif choice == 3:
            print("Thankyou for playing.")
            break




