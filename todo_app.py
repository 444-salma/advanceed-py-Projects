from todo_list import ToDoList

class ToDoApp:
    def __init__(self):
        self.todo_list = ToDoList()

    def run(self):
        print("Welcome to the To-Do List App")

        while True:
            print("\nChoose an operation: add, view, remove, exit")
            operation = input("Enter operation: ").lower().strip()

            if operation == "add":
                task = input("Enter the task: ").strip()
                print(self.todo_list.add_task(task))

            elif operation == "view":
                for line in self.todo_list.view_tasks():
                    print(line)

            elif operation == "remove":
                task = input("Enter the task to remove: ").strip()
                print(self.todo_list.remove_task(task))

            elif operation == "exit":
                print("Goodbye 👋")
                break

            else:
                print("Invalid operation. Please choose: add, view, remove, or exit.")
