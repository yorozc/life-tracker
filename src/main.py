import sqlite3
from queries import CREATE_TASK_TABLE
from interface import userInterface

def init_db():
    conn = sqlite3.connect("src/tasks.db")
    cursor = conn.cursor()
    cursor.execute(CREATE_TASK_TABLE)
    conn.commit()
    conn.close()

def main():
    user = userInterface()
    user.mainInterface()

if __name__=="__main__":
    init_db()
    main()