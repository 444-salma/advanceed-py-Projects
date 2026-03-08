class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not task:
            return "Task cannot be empty."
        self.tasks.append(task)
        return f'Task "{task}" added successfully.'

    def remove_task(self, task):
        if not self.tasks:
            return "Your to-do list is empty. Nothing to remove."
        if task in self.tasks:
            self.tasks.remove(task)
            return f'Task "{task}" removed successfully.'
        return f'Task "{task}" not found in your to-do list.'

    def view_tasks(self):
        if not self.tasks:
            return ["Your to-do list is empty."]
        return [f"{i}. {task}" for i, task in enumerate(self.tasks, start=1)]
