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
        return Task(
            d["id"], d["title"], d["completed"],
            d["tags"], d["created"], d["updated"]
        )

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
        if not os.path.exists(DATA_FILE):
            self.log("No data file found; starting fresh.")
            return
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
            tasks_data = data.get("tasks", [])
            self.counter = int(data.get("counter", self.counter))
            self.tasks = [Task.from_dict(d) for d in tasks_data]
            self.log(f"Loaded {len(self.tasks)} tasks from disk.")
        except (json.JSONDecodeError, ValueError, TypeError) as e:
            self.tasks = []
            self.counter = 1
            self.log(f"ERROR loading tasks: {e}. Starting with empty task list.")

    def save(self):
        with open(DATA_FILE, "w") as f:
            json.dump(
                {"tasks": [t.to_dict() for t in self.tasks], "counter": self.counter},
                f,
                indent=2
            )
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

    # -----------------------------
    # NEW FEATURE: EDIT TASK
    # -----------------------------
    def edit_task(self, id, new_title):
        for t in self.tasks:
            if t.id == id:
                old_title = t.title
                t.title = new_title
                t.updated = datetime.datetime.now().isoformat()
                self.save()
                self.log(f"Edited task {id}: '{old_title}' → '{new_title}'")
                print("Updated:", t)
                return
        print("Task not found.")

    # -----------------------------
    # NEW FEATURE: EXPORT TASKS TO TXT
    # -----------------------------
    def export_txt(self, filename="tasks_export.txt"):
        with open(filename, "w") as f:
            for t in self.tasks:
                status = "DONE" if t.completed else "TODO"
                line = f"{t.id}. [{status}] {t.title} (tags: {', '.join(t.tags)})\n"
                f.write(line)
        self.log(f"Exported tasks to {filename}")
        print(f"Exported tasks to {filename}")

    # -----------------------------
    # NEW FEATURE: STATS
    # -----------------------------
    def stats(self):
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t.completed])
        pending = total - completed
        percent = (completed / total * 100) if total else 0

        tag_count = {}
        for t in self.tasks:
            for tag in t.tags:
                tag_count[tag] = tag_count.get(tag, 0) + 1

        print("\n=== Task Stats ===")
        print(f"Total tasks: {total}")
        print(f"Completed: {completed}")
        print(f"Pending: {pending}")
        print(f"Completion: {percent:.1f}%")

        if tag_count:
            print("\nTags:")
            for tag, count in tag_count.items():
                print(f"  #{tag}: {count}")
        else:
            print("No tags defined.")
        print("=================\n")


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
        print("9) Edit Task")
        print("10) Export Tasks to TXT")
        print("11) Show Stats")
        
        choice = input("> ").strip()
        
        if choice == "1":
            title = input("Title: ").strip()
            tags = input("Tags (comma): ").strip().split(",") if input("Add tags? (y/n): ").strip().lower() == "y" else []
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
        elif choice == "9":
            mgr.edit_task(int(input("ID: ")), input("New title: "))
        elif choice == "10":
            mgr.export_txt()
        elif choice == "11":
            mgr.stats()
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()
