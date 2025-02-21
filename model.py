import requests as req
import json
import mysql.connector
import re
from hashlib import sha256

class Model():
    def __init__(self,db_connection):
        word = None
        word_data = None
        self.db = db_connection
        self.setup_database()

    def setup_database(self):
        self.db.cursor.execute("""
                               CREATE TABLE IF NOT EXISTS users(id int primary key auto_increment,username varChar(255),password varChar(255),score int)
                               """)
        self.db.conn.commit()
        print("Table maybe created?")

    def get_word_json(self):

        for _ in range(10):
            try:
                response = req.get("https://random-word-api.herokuapp.com/word",timeout=0.1)
                response = response.json()
                response = req.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+response[0],timeout=0.4)
                response = response.json()
                if response[0]["word"]:
                    return response
            except Exception as e:
                print(f"Error: {e}")
            else:
                break

        raise Exception("Data not found")
    
    def set_word(self, word):
        self.word = word
    def set_data(self, data):
        self.word_data = data

    def create_user(self,username,password):
        self.db.cursor.execute("SELECT * FROM users WHERE username = %s",(username,))
        result = self.db.cursor.fetchall()
        if result:
            return False, "Name already in use. Please select another."
        else:
            print("Før password check")
            if not self.password_is_valid(password):
                return False, "Your password is not valid.\nMinimum of 6 characters,Max 12, at least one letter,one number and one special character."
            else:
                password = sha256(password.encode('utf-8')).hexdigest()
                self.db.cursor.execute("INSERT INTO users(username,password,score) VALUES(%s,%s,0)",(username,password))
                self.db.conn.commit()
                return True, "User Created"
    
    def login_user(self,username,password):
        self.db.cursor.execute("SELECT password FROM users WHERE username = %s LIMIT 1",(username,))
        result = self.db.cursor.fetchone()[0]
        if result:
            if sha256(password.encode('utf-8')).hexdigest() == result:
                return True, "You're logged in"
            else:
                return False, "Wrong password"
        else:
            return False, "User not found"
        
    def password_is_valid(self,password):
        #Minimum six characters, Max 12, at least one letter, one number and one special character
        match = re.match("^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{6,12}$",password)
        return match

    def get_score(self,username):
        self.db.cursor.execute("SELECT score FROM users WHERE username = %s LIMIT 1",(username,))
        result = self.db.cursor.fetchone()[0]
        if result or result == 0:
            return result
        else: 
            raise Exception("None value")


    def set_score(self,username,newscore):
        self.db.cursor.execute("UPDATE users SET score = %s WHERE username = %s ",(newscore,username))
        self.db.conn.commit()

    def add_score(self,username,increment):
        score = self.get_score(username)
        newscore = score + increment
        self.set_score(username,newscore)

        
