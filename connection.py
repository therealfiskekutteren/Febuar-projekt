import mysql.connector

class Connection():

    _instance = None
    conn = None


    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self.conn is None:
            try:
                self.conn = mysql.connector.connect(
                    host="localhost",
                    database="userdb",
                    user="root",
                    password=""
                )
                if self.conn.is_connected():
                    db_info = self.conn.get_server_info()
                    print("Connected to MySQL server version: " ,db_info)
                    self.cursor = self.conn.cursor()
                    self.cursor.execute("SELECT database()")
                    record = self.cursor.fetchone()
                    print("You are now connected to database: ",record[0])
            except mysql.connector.Error as e:
                print("Error while connecting to MySQL:"+e)
        else:
            print("Connection already exists")