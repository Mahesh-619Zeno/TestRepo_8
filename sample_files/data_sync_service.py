from __future__ import annotations

import json
import datetime
from pathlib import Path
from typing import List, Optional, Dict, Any


DATA_FILE = Path("tasks.json")
LOG_FILE = Path("task_manager.log")


# ----------------------------
# Helpers
# ----------------------------
def now_iso() -> str:
    return datetime.datetime.now().isoformat()


def safe_read_json(path: Path) -> Dict[str, Any]:
    if not path.exists() or path.read_text().strip() == "":
        return {}
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError:
        return {}  # corrupted file → ignore


def append_log(message: str):
    LOG_FILE.write_text(
        (LOG_FILE.read_text() if LOG_FILE.exists() else "")
        + f"{now_iso()} {message}\n"
    )


# ----------------------------
# Task Model
# ----------------------------
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

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "tags": self.tags,
            "created": self.created,
            "updated": self.updated,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Task":
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
        tags = ",".join(self.tags)
        return f"[{self.id}] {status} {self.title} (tags: {tags})"


# ----------------------------
# Task Manager
# ----------------------------
class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []
        self.counter: int = 1
        self.load()

    # ------------------------
    # Persistence
    # ------------------------
    def load(self):
        data = safe_read_json(DATA_FILE)
        self.counter = int(data.get("counter", 1))
        self.tasks = [Task.from_dict(t) for t in data.get("tasks", [])]
        self.tasks.sort(key=lambda x: x.id)
        append_log(f"Loaded {len(self.tasks)} tasks.")

    def save(self):
        data = {
            "tasks": [t.to_dict() for t in self.tasks],
            "counter": self.counter,
        }
        DATA_FILE.write_text(json.dumps(data, indent=2))
        append_log("Saved tasks.")

    # ------------------------
    # Helpers
    # ------------------------
    def find_task(self, id: int) -> Optional[Task]:
        return next((t for t in self.tasks if t.id == id), None)

    # ------------------------
    # CRUD Operations
    # ------------------------
    def add_task(self, title: str, tags: List[str]):
        clean_tags = [t.strip() for t in tags if t.strip()]
        task = Task(self.counter, title, False, clean_tags)
        self.tasks.append(task)
        self.counter += 1
        self.save()
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
        print("Completed:", task)

    def delete_task(self, id: int):
        task = self.find_task(id)
        if not task:
            print("Task not found.")
            return
        self.tasks.remove(task)
        self.save()
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
        print("Updated:", task)


# ----------------------------
# Menu System
# ----------------------------
def menu():
    mgr = TaskManager()

    while True:
        print("\n== Task Manager ==")
        print("1) Add Task")
        print("2) List Uncompleted")
        print("3) List All")
        print("4) Complete Task")
        print("5) Delete Task")
        print("6) Search")
        print("7) Add Tags")
        print("8) Exit")

        choice = input("> ").strip()

        try:
            if choice == "1":
                title = input("Title: ").strip()
                tags = input("Tags (comma): ").split(",")
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
                id = int(input("ID: "))
                tags = input("Tags (comma): ").split(",")
                mgr.tag_task(id, tags)

            elif choice == "8":
                print("Bye!")
                break

            else:
                print("Invalid choice.")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    menu()