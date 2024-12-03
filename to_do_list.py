import os
import json
from datetime import datetime

class ToDoListApp:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, title, description):
        task = {
            "title": title,
            "description": description,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "completed": False
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nTasks:")
        for idx, task in enumerate(self.tasks, start=1):
            status = "[Completed]" if task["completed"] else "[Pending]"
            print(f"{idx}. {task['title']} {status} - {task['description']} (Created: {task['created_at']})")

    def update_task(self, task_number, title=None, description=None, completed=None):
        if 1 <= task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if completed is not None:
                task["completed"] = completed
            self.save_tasks()
            print(f"Task {task_number} updated successfully.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"Task '{removed_task['title']}' deleted successfully.")
        else:
            print("Invalid task number.")

    def clear_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task["completed"]]
        self.save_tasks()
        print("All completed tasks cleared.")

if __name__ == "__main__":
    app = ToDoListApp()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Clear Completed Tasks")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            app.add_task(title, description)
        elif choice == "2":
            app.list_tasks()
        elif choice == "3":
            app.list_tasks()
            try:
                task_number = int(input("Enter task number to update: "))
                title = input("Enter new title (or press Enter to skip): ") or None
                description = input("Enter new description (or press Enter to skip): ") or None
                completed = input("Mark as completed? (yes/no): ").strip().lower()
                completed = True if completed == "yes" else False if completed == "no" else None
                app.update_task(task_number, title, description, completed)
            except ValueError:
                print("Invalid input.")
        elif choice == "4":
            app.list_tasks()
            try:
                task_number = int(input("Enter task number to delete: "))
                app.delete_task(task_number)
            except ValueError:
                print("Invalid input.")
        elif choice == "5":
            app.clear_completed_tasks()
        elif choice == "6":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
