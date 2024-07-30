class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: str):
        if task and task not in self.tasks:
            self.tasks.append(task)

    def remove_task(self, task: str):
        if task in self.tasks:
            self.tasks.remove(task)

    def list_tasks(self):
        return self.tasks

