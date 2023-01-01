import mysql.connector


class User_db:

    def __init__(self):
        self.con = mysql.connector.connect(host="localhost", user="root", password="yonasamare7", database="yonidb")
        query = "create table if not exists user(userid int primary key,username varchar(200),password varchar(20))"
        my_cursor = self.con.cursor()
        my_cursor.execute(query)

    def insert_user(self, userid, username, password):
        query = "insert into user(userid, username, password)values({},'{}','{}')".format(userid, username, password)
        print(query)
        my_cursor = self.con.cursor()
        my_cursor.execute(query)
        self.con.commit()

    def fetch_all(self):
        query = "select * from user"
        my_curser = self.con.cursor()
        my_curser.execute(query)
        for row in my_curser:
            print(row)
            print("userid: ", row[0])
            print("username: ", row[1])
            print("password: ", row[2])
            print()
            print()

    def fetch_one(self, id):
        query = "select * from user where userid={}".format(id)
        my_curser = self.con.cursor()
        my_curser.execute(query)
        for row in my_curser:
            print(row)
            print("userid: ", row[0])
            print("username: ", row[1])
            print("password: ", row[2])

    def delete_user(self, userid):
        query = "delete from user where userid= {}".format(userid)
        print(query)
        my_cursor = self.con.cursor()
        my_cursor.execute(query)
        self.con.commit()

    def update_user(self, userid, newusername, newpassword):
        query = "update user set userid{}, username={} where password{}".format(userid, newusername, newpassword)
        print(query)
        my_cursor = self.con.cursor()
        my_cursor.execute(query)
        self.con.commit()

    def checkuser(self, username, password):
        query = "select * from user where username='{}' and password='{}'".format(username, password)
        my_curser = self.con.cursor()
        my_curser.execute(query)
        for row in my_curser:
            print('Welcome User: ', row[1])
            break
        else:
            print("Invalid User")


# user_db = User_db()
# # user_db.insert_user(1, "yonas", "1234")
# # user_db.insert_user(2, "dave", "1234")
# # user_db.insert_user(3, "heni", "1234")
# # user_db.insert_user(4, "negae", "1234")
# # user_db.fetch_all()
# # user_db.delete_user(1992)
# user_db.checkuser("yonas", 1234)


class question():

    def __init__(self):
        self.con = mysql.connector.connect(host="localhost", user="root", password="yonasamare7", database="yonidb")
        query = "create table if not exists trivia(Id int(20) primary key, Category varchar(250), Question varchar(250),Choice1 varchar(100), Choice2 varchar(100), Choice3 varchar(100), Choice4 varchar(100), Answer varchar(100))"
        my_cursor = self.con.cursor()
        my_cursor.execute(query)

    def insert_question(self, ID, Category, Question, Choice1, Choice2, Choice3, Choice4, Answer):
        query = "insert into trivia values({},'{}','{}','{}','{}','{}','{}','{}')".format(ID, Category, Question,
                                                                                          Choice1, Choice2, Choice3,
                                                                                          Choice4, Answer)
        my_cursor = self.con.cursor()
        my_cursor.execute(query)
        self.con.commit()

    def fetch_question(self):
        query = "select * from trivia"
        my_curser = self.con.cursor()
        my_curser.execute(query)
        for row in my_curser:
            print("ID: ", row[0])
            print("Category: ", row[1])
            print("Question: ", row[2])
            print("Choice1: ", row[3])
            print("Choice2: ", row[4])
            print("Choice3: ", row[5])
            print("Choice4: ", row[6])
            print("Answer: ", row[7])
            print()


class players():

    def __init__(self):
        self.con = mysql.connector.connect(host="localhost", user="root", password="yonasamare7", database="yonidb")
        query = "create table if not exists player(player_name varchar(50), score int )"
        my_curser = self.con.cursor()
        my_curser.execute(query)

    def fetch_query(self, player_name, score):
        query = "insert into player values('{}',{})".format(player_name, score)
        my_curser = self.con.cursor()
        my_curser.execute(query)
        self.con.commit()

        query_category = "select distinct(Category) from trivia"
        my_curser = self.con.cursor()
        my_curser.execute(query_category)
        print("please select category for the trivia game")
        for i in my_curser:
            print(i[0])
        category_input = input("Enter Category: ")
        print()
        query = "select * from trivia where Category='{}'".format(category_input)
        my_curser = self.con.cursor()
        my_curser.execute(query)
        score = 0
        for row in my_curser:
            print("Question: ", row[2])
            print("Choice 1: ", row[3])
            print("Choice 2: ", row[4])
            print("Choice 3: ", row[5])
            print("Choice 4: ", row[6])
            print()
            num = (input(f"Enter options : "))
            if num not in row[7]:
                print("incorrect")
            else:
                score += 1

        query1 = "update player set score={} where player_name='{}'".format(score, player_name)
        my_curser = self.con.cursor()
        my_curser.execute(query1)
        self.con.commit()
        print()
        print("***** Your result *****")
        print("player: ", player_name)
        print("score: ", score)
        print()
        solution = input("Do you want to see solutions? press 0 to exit | press 1 for solutions: ")
        if solution == 1:
            query = "select * from trivia where Category='{}'".format(solution)
            my_curser = self.con.cursor()
            my_curser.execute(query)
            print()
            print("The correct answer are")
            print()
            for row in my_curser:
                print("Question: ", row[2])
                print("option1: ", row[3])
                print("option2: ", row[4])
                print("option3: ", row[5])
                print("option4: ", row[6])
                print("Answer for given question is: ", row[7])
                print()


class Show_user_score:
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost", user="root", password="yonasamare7", database="yonidb")
        query = "select player_name, score from player order by score desc "
        my_curser = self.con.cursor()
        my_curser.execute(query)
        for row in my_curser:
            print("player name: ", row[0])
            print("player score: ", row[1])
            print()
