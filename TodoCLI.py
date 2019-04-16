import os
import sqlite3

DEFAULT_PATH = os.path.join(os.path.dirname(__file__),'tododatabase1.sqlite3')
def db_Connect(db_path=DEFAULT_PATH): 
   connection = sqlite3.connect(db_path)
   return connection

def db_Create(): 
    conn= db_Connect()
    try:
      cur= conn.cursor()
      sql =""" CREATE TABLE IF NOT EXISTS todos (
       id INTEGER PRIMARY KEY,
        todo_text TEXT NOT NULL 
        ) 
        """
      cur.execute(sql)
      print("table created ")
    except Error as e:
        print(e)
    conn.close()


def add_todo(todo_text): 
   conn = db_Connect()
   cur = conn.cursor()
   sql1="""INSERT INTO todos (todo_text) VALUES (?) """
   cur.execute(sql1, (todo_text,))
   conn.commit()
   
   selectSQL=""" SELECT * FROM todos """
   cur.execute(selectSQL)

   results = cur.fetchall()
   for row in results: 
      print(row)
   conn.close() 


db_Create()
add_todo("go to school??") 








