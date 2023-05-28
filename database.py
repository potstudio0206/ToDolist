import sqlite3

class Database:
    def __init__(self, db_name="tasks.db"):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT)"
        )

    def add_task(self, task):
        self.cur.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        self.conn.commit()

    def delete_task(self, task):
        self.cur.execute("DELETE FROM tasks WHERE task=?", (task,))
        self.conn.commit()

    def edit_task(self, old_task, new_task):
        self.cur.execute(
            "UPDATE tasks SET task=? WHERE task=?", (new_task, old_task)
        )
        self.conn.commit()

    def get_tasks(self):
        self.cur.execute("SELECT task FROM tasks")
        return self.cur.fetchall()
