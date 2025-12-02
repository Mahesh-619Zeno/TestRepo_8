from __future__ import annotations
from pathlib import Path
import json
import datetime
from typing import List, Optional

DATA_FILE = Path("tasks.json")
LOG_FILE = Path("task_manager.log")


def now_iso() -> str:
    return datetime.datetime.now().isoformat()


class Task:
    def __init__(
        self,
        id: int,
        title: str,
        completed: bool = False,
        tags: Optional[List[str]] = None,
        created: Optional[str] = None,
        updated: Optional[str] = None,
    ):
        self.id = id
        self.title = title
        self.completed = completed
        self.tags = tags or []
        self.created = created or now_iso()
        self.updated = updated or self.created

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "tags": self.tags,
            "created": self.created,
            "updated": self.updated,
        }

    @staticmethod
    def from_dict(d: dict) -> "Task":
        return Task(
            id=d["id"],
            title=d["title"],
            completed=d.get("completed", False),
            tags=d.get("tags", []),
            created=d.get("created"),
            updated=d.get("updated"),
        )

    def __str__(self) -> str:
        status = "✅" if self.completed else "❌"
        tag_str = ",".join(self.tags)
        return f"[{self.id}] {status} {self.title} (tags: {tag_str})"


class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []
        self.counter: int = 1
        self.load()

    # ------------------------
    # Persistence
    # ------------------------
    def load(self):
        if not DATA_FILE.exists():
            self.log("No data file found; starting fresh.")
            return

        try:
            data = json.loads(DATA_FILE.read_text())
            self.counter = int(data.get("counter", 1))
            self.tasks = [Task.from_dict(t) for t in data.get("tasks", [])]

            # Optional: keep tasks sorted by ID
            self.tasks.sort(key=lambda t: t.id)

            self.log(f"Loaded {len(self.tasks)} tasks.")
        except Exception as e:
            self.tasks = []
            self.counter = 1
            self.log(f"ERROR loading tasks: {e}")

    def save(self):
        DATA_FILE.write_text(
            json.dumps(
                {
                    "tasks": [t.to_dict() for t in self.tasks],
                    "counter": self.counter,
                },
                indent=2,
            )
        )
        self.log("Saved tasks to disk.")

    def log(self, message: str):
        LOG_FILE.write_text(
            LOG_FILE.read_text() + f"{now_iso()} {message}\n"
            if LOG_FILE.exists()
            else f"{now_iso()} {message}\n"
        )

    # ------------------------
    # Helpers
    # ------------------------
    def find_task(self, id: int) -> Optional[Task]:
        return next((t for t in self.tasks if t.id == id), None)

    # ------------------------
    # CRUD / Actions
    # ------------------------
    def add_task(self, title: str, tags: List[str]):
        tags = [t.strip() for t in tags if t.strip()]
        task = Task(self.counter, title, False, tags)
        self.tasks.append(task)
        self.counter += 1
        self.save()
        self.log(f"Added task {task.id}: {title}")
        print("Task added:", task)

    def list_tasks(self, show_all: bool = False):
        filtered = self.tasks if show_all else [t for t in self.tasks if not t.completed]
        if not filtered:
            print("🗒️ No tasks.")
        for t in filtered:
            print(t)

    def complete_task(self, id: int):
        task = self.find_task(id)
        if not task:
            print("Task not found.")
            return

        task.completed = True
        task.updated = now_iso()
        self.save()
        self.log(f"Completed task {id}")
        print("Completed:", task)

    def delete_task(self, id: int):
        task = self.find_task(id)
        if not task:
            print("Task not found.")
            return

        self.tasks.remove(task)
        self.save()
        self.log(f"Deleted task {id}")
        print("Deleted:", task)

    def search(self, term: str):
        term = term.lower().strip()
        found = [t for t in self.tasks if term in t.title.lower()]

        if not found:
            print(f"No tasks found matching '{term}'.")
        else:
            for t in found:
                print(t)

    def tag_task(self, id: int, tags: List[str]):
        task = self.find_task(id)
        if not task:
            print("Task not found.")
            return

        cleaned = [t.strip() for t in tags if t.strip()]
        task.tags = sorted(set(task.tags + cleaned))
        task.updated = now_iso()
        self.save()
        self.log(f"Tagged task {id} with {cleaned}")
        print("Updated:", task)


# ------------------------
# Menu
# ------------------------
def menu():
    mgr = TaskManager()

    options = {
        "1": lambda: mgr.add_task(
            input("Title: ").strip(),
            input("Tags (comma): ").split(",") if input("Add tags? (y/n): ").lower() == "y" else [],
        ),
        "2": lambda: mgr.list_tasks(show_all=False),
        "3": lambda: mgr.list_tasks(show_all=True),
        "4": lambda: mgr.complete_task(int(input("ID: "))),
        "5": lambda: mgr.delete_task(int(input("ID: "))),
        "6": lambda: mgr.search(input("Search term: ")),
        "7": lambda: mgr.tag_task(
            int(input("ID: ")), input("Tags (comma): ").split(",")
        ),
    }

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
        if choice == "8":
            print("Bye!")
            break

        action = options.get(choice)
        if action:
            try:
                action()
            except Exception as e:
                print("Error:", e)
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()
