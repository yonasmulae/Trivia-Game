from dbview import *


def main1():
    print("1. Admin Details")
    print("2. quiz details")
    choice = int(input("Press 1 for Admin and Press 2 for question: "))
    if choice == 1:
        db_view()
    elif choice == 2:
        Question_details()


def check_admin():
    checkAdmin()
    main1()

