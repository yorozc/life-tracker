import sqlite3

conn = sqlite3.connect('src/task.db')

c = conn.cursor() #used to run sql commands

#create task table
c.execute("""create table tasks (
            taskName text,
            description text,
            checked, integer,
            data, blob
          )""")

conn.commit()

conn.close()