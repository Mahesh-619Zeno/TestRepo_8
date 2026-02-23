
import os
import json
import datetime

DATA_FILE = "tasks.json"
LOG_FILE = "task_manager.log"
class Task:
    def __init__(self, id, title, completed=False, tags=None, created=None, updated=None):
        self.id = id
        self.title = title
        self.completed = completed
        self.tags = tags or []
        self.created = created or datetime.datetime.now().isoformat()
        self.updated = updated or self.created

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "tags": self.tags,
            "created": self.created,
            "updated": self.updated,
        }

    @staticmethod
    def from_dict(d):
        return Task(d["id"], d["title"], d["completed"], d["tags"], d["created"], d["updated"])

    def __str__(self):
        status = "✅" if self.completed else "❌"
        tags = ",".join(self.tags)
        return f"[{self.id}] {status} {self.title} (tags: {tags})"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.counter = 1
        self.load()

    def load(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(d) for d in data.get("tasks", [])]
                self.counter = data.get("counter", self.counter)
            self.log("Loaded tasks from disk.")
        else:
            self.log("No data file found; starting fresh.")

    def save(self):
        with open(DATA_FILE, "w") as f:
            json.dump({"tasks": [t.to_dict() for t in self.tasks], "counter": self.counter}, f, indent=2)
        self.log("Saved tasks to disk.")

    def log(self, message):
        with open(LOG_FILE, "a") as f:
            f.write(f"{datetime.datetime.now().isoformat()} {message}\n")

    def add_task(self, title, tags=None):
        task = Task(self.counter, title, False, tags or [])
        self.tasks.append(task)
        self.counter += 1
        self.save()
        self.log(f"Added task {task.id}: {title}")
        print("Task added:", task)

    def list_tasks(self, show_all=False):
        if not self.tasks:
            print("🗒️ No tasks.")
            return
        for t in self.tasks:
            if show_all or not t.completed:
                print(t)

    def complete_task(self, id):
        for t in self.tasks:
            if t.id == id:
                t.completed = True
                t.updated = datetime.datetime.now().isoformat()
                self.save()
                self.log(f"Completed task {id}")
                print("Completed:", t)
                return
        print("Task not found.")

    def delete_task(self, id):
        for i, t in enumerate(self.tasks):
            if t.id == id:
                self.tasks.pop(i)
                self.save()
                self.log(f"Deleted task {id}")
                print("Deleted:", t)
                return
        print("Task not found.")

    def search(self, term):
        found = [t for t in self.tasks if term.lower() in t.title.lower()]
        if not found:
            print("No tasks found matching", term)
        else:
            for t in found:
                print(t)

    def tag_task(self, id, tags):
        for t in self.tasks:
            if t.id == id:
                t.tags = list(set(t.tags + tags))
                t.updated = datetime.datetime.now().isoformat()
                self.save()
                self.log(f"Tagged task {id} with {tags}")
                print("Updated:", t)
                return
        print("Task not found.")

def menu():
    mgr = TaskManager()
    while True:
        print("\n== Task Manager ==")
        print("1) Add Task")
        print("2) List Tasks (uncompleted)")
        print("3) List All Tasks")
        print("4) Complete Task")
        print("5) Delete Task")
        print("6) Search Tasks")
        print("7) Tag Task")
        print("8) Exit")
        choice = input("> ").strip()
        if choice == "1":
            title = input("Title: ").strip()
            tags = input("Tags (comma): ").strip().split(",") if input("Add tags? (y/n): ").strip().lower()=="y" else []
            mgr.add_task(title, tags)
        elif choice == "2":
            mgr.list_tasks(show_all=False)
        elif choice == "3":
            mgr.list_tasks(show_all=True)
        elif choice == "4":
            mgr.complete_task(int(input("ID: ")))
        elif choice == "5":
            mgr.delete_task(int(input("ID: ")))
        elif choice == "6":
            mgr.search(input("Search term: "))
        elif choice == "7":
            mgr.tag_task(int(input("ID: ")), input("Tags (comma): ").split(","))
        elif choice == "8":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
