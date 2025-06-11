CREATE_TASK_TABLE = """
create table if not exists tasks(
            taskName text,
            description text,
            checked integer,
            date blob);
"""
INSERT_TASK = """
INSERT INTO tasks (taskName, description, checked, date) VALUES (?, ?, ?, ?);
"""

GET_ALL_TASKS = "select * from tasks;"