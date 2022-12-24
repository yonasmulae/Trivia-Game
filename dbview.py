from db import *


def db_view():
    db = User_db
    print("********** Welcome to Admin section **********")
    print()
    while True:
        print("press 1 to Insert New_user")
        print("press 2 to Display Single user")
        print("press 3 to display All user")
        print("press 4 to Delete a User")
        print("press 5 to Update a User")
        print("press 6 to EXIT")
        print()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("To insert a new user fill the details: ")
            user_id = int(input("user_id: "))
            user_name = input("user_name: ")
            password = int(input("password: "))
            db.insert_user(user_id, user_name, password)

        elif choice == 2:
            user_id = input("To display user enter user_id: ")
            db.fetch_one(int(user_id))

        elif choice == 3:
            print("Details in db")
            print()
            db.fetch_all()

        elif choice == 4:
            user_id = int(input("To delete a user kindly give the userid: "))
            db.delete_user(int(user_id))

        elif choice == 5:
            print("To update a user fill the details")
            user_id = int(input("user_id: "))
            user_name = input("user_name: ")
            password = int(input("password: "))
            db.update_user(user_id, user_name, password)

        elif choice == 6:
            break
        else:
            print("Invalid Input! Try again.")


def Question_details():
    Q = question()
    print("********** Welcome to Quiz Section **********")
    print()
    while True:
        print("Press 1 to Insert New Question.")
        print("Press 2 to print Question.")
        print("Press 3 to Exit.")
        print()

        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("To Insert New Question fill the details")
            question_id = int(input("Enter question Id: "))
            question_Category = input("Enter the question Category: ")
            question_q = input("Enter the Question: ")
            choice1 = input("Enter the Choice1: ")
            choice2 = input("Enter the Choice2: ")
            choice3 = input("Enter the Choice3: ")
            choice4 = input("Enter the Choice4: ")
            Answer = input("Enter the Answer: ")
            Q.insert_question(question_id, question_Category, question_q, choice1, choice2, choice3, choice4, Answer)
        elif choice == 2:
            print("Questions in Trivia Game")
            print()
            Q.fetch_question()
        elif choice == 3:
            break
        else:
            print("Invalid Input! Try Again.")


def question_view():
    Question = players()
    print("********** Welcome to Play Game Section **********")
    print()
    while True:
        print("Press 1 to Play the Game")
        print("Press 2 to Exit")
        print()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            playname = input("Enter your name to get started ? ")
            Question.fetch_query(playname, 0)
        else:
            break


def Scores():
    print("********** Players and Their Scores **********")
    print()
    Show_user_score()


def checkAdmin():
    username = input("Enter Admin User_name: ")
    password = input("Enter Admin Password: ")
    admin = User_db()
    check = admin.checkuser(username, password)
    return check
