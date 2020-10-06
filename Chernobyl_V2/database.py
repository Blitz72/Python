import sqlite3 as db

db_path = '/home/pi/Python/Chernobyl_V2/db/Chernobyl.db'

class Database:
    
    def __init__(self, path):
        self.connection = db.connect(path)
    
    def __enter__(self):
        self.c = self.connection.cursor()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
        print('Connection closed.')
    
    def update():
        pass
    


with Database(db_path):
    print('Sweet!')