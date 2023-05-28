from database import Database

class TaskManager:
    def __init__(self, db):
        self.db = db

    def add_task(self, task):
        self.db.add_task(task)

    def delete_task(self, task):
        self.db.delete_task(task)

    def edit_task(self, old_task, new_task):
        self.db.edit_task(old_task, new_task)

    def get_tasks(self):
        return [task[0] for task in self.db.get_tasks()]
