import sqlite3 as db
from supported_colors import supported_colors_list


class Database:
    
    def __init__(self, path, command):
        self.path = path
        self.command = command
        self.connection = db.connect(self.path)
        if self.connection:
            print('Connected to: ', path)
    
    def __enter__(self):
        self.c = self.connection.cursor()
        return self.c.execute(self.command).fetchone()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
#        print('Connection committed.')
        self.connection.close()
#        print('Connection closed.')


if __name__ == '__main__':
    db_path = '/home/pi/Python/VoiceTTS/db/Voice.db'
    connection = db.connect(db_path)
    c = connection.cursor()

    # c.execute('DROP TABLE IF EXISTS supported_colors')
    # c.execute('''CREATE TABLE IF NOT EXISTS supported_colors (color_id INTEGER PRIMARY KEY, name VARCHAR(50))''')
    # c.execute('''CREATE TABLE IF NOT EXISTS alexa (color_id INTEGER FOREIGN KEY AUTOINCREMENT, is_rgb BOOLEAN, 
    #             tcs_brt INTEGER, m FLOAT, b INTEGER, )''')
    # c.execute('''CREATE TABLE IF NOT EXISTS google (color_id INTEGER FOREIGN KEY, is_rgb BOOLEAN, 
    #             tcs_brt INTEGER, tcs_r INTEGER, tcs_g INTEGER, tcs_b INTEGER, m FLOAT, b INTEGER)''')
    # c.execute('''INSERT INTO supported_colors (name) VALUES ('alice blue')''')
    items = c.execute('''SELECT * FROM supported_colors''')
    for item in items:
        print(item)


    connection.commit()
