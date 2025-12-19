import os
import sys
import math, statistics
import json
import time
import uuid
import random
import logging
import datetime
import threading
import itertools
import functools
from dataclasses import dataclass, field
from typing import List, Dict, Callable, Optional

# -----------------------------
# Logging Setup
# -----------------------------
logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    datefmt="%H:%M:%S"
)

logger = logging.getLogger(__name__)

# -----------------------------
# Data Models
# -----------------------------

@dataclass
class Task:
    id: str
    title: str
    completed: bool = False
    created_at: datetime.datetime = field(default_factory=datetime.datetime.utcnow)

    def complete(self):
        logger.debug(f"Completing task {self.id}")
        self.completed = True

    def serialize(self) -> Dict:
        logger.debug(f"Serializing task {self.id}")
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "created_at": self.created_at.isoformat()
        }


@dataclass
class User:
    id: str
    username: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, title: str) -> Task:
        logger.debug(f"User '{self.username}' adding task: {title}")
        task = Task(id=str(uuid.uuid4()), title=title)
        self.tasks.append(task)
        return task

    def serialize(self) -> Dict:
        logger.debug(f"Serializing user {self.username}")
        return {
            "id": self.id,
            "username": self.username,
            "tasks": [t.serialize() for t in self.tasks]
        }

# -----------------------------
# Utility Functions
# -----------------------------

def load_json_file(path: str) -> Dict:
    logger.debug(f"Loading JSON file: {path}")
    if not os.path.exists(path):
        logger.warning(f"File not found: {path}. Returning empty dict.")
        return {}
    with open(path, "r") as f:
        return json.load(f)


def save_json_file(path: str, data: Dict):
    logger.debug(f"Saving JSON data to file: {path}")
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def generate_random_username() -> str:
    adjectives = ["fast", "silent", "happy", "wild", "lucky"]
    animals = ["lion", "tiger", "cat", "eagle", "bear"]
    username = random.choice(adjectives) + "_" + random.choice(animals)
    logger.debug(f"Generated username: {username}")
    return username


def slow_operation(seconds: int):
    logger.debug(f"Starting slow operation for {seconds} seconds")
    time.sleep(seconds)
    logger.debug("Slow operation finished")


def threaded_worker(task_func: Callable, *args, **kwargs):
    logger.debug("Starting threaded worker")
    thread = threading.Thread(target=task_func, args=args, kwargs=kwargs)
    thread.start()
    return thread


def calculate_statistics(numbers: List[int]) -> Dict:
    logger.debug("Calculating statistics")
    if not numbers:
        return {"mean": None, "min": None, "max": None}
    return {
        "mean": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "median": statistics.median(numbers) if numbers else None,
        "stdev": statistics.stdev(numbers) if len(numbers) > 1 else None
    }

# -----------------------------
# Task Manager Class
# -----------------------------

class TaskManager:
    def __init__(self, storage_path="tasks.json"):
        logger.debug("Initializing TaskManager")
        self.storage_path = storage_path
        self.users: Dict[str, User] = {}
        self.load()

    def create_user(self, username: Optional[str] = None) -> User:
        username = username or generate_random_username()
        user = User(id=str(uuid.uuid4()), username=username)
        logger.info(f"Created user: {username}")
        self.users[user.id] = user
        return user

    def find_user(self, user_id: str) -> Optional[User]:
        logger.debug(f"Finding user with ID: {user_id}")
        return self.users.get(user_id)

    def add_task_to_user(self, user_id: str, title: str) -> Optional[Task]:
        user = self.find_user(user_id)
        if not user:
            logger.error("User not found.")
            return None
        task = user.add_task(title)
        logger.info(f"Added task '{title}' to user {user.username}")
        return task

    def list_all_tasks(self) -> List[Task]:
        logger.debug("Listing all tasks")
        return list(itertools.chain.from_iterable(u.tasks for u in self.users.values()))

    def save(self):
        logger.debug("Saving all user data")
        data = {uid: user.serialize() for uid, user in self.users.items()}
        save_json_file(self.storage_path, data)

    def load(self):
        logger.debug("Loading user data")
        data = load_json_file(self.storage_path)
        for uid, udata in data.items():
            user = User(id=udata["id"], username=udata["username"])
            for tdata in udata.get("tasks", []):
                task = Task(
                    id=tdata["id"],
                    title=tdata["title"],
                    completed=tdata["completed"],
                    created_at=datetime.datetime.fromisoformat(tdata["created_at"])
                )
                user.tasks.append(task)
            self.users[uid] = user

# -----------------------------
# CLI Interface
# -----------------------------

def print_menu():
    print("\n=== Task Manager CLI ===")
    print("1. Create User")
    print("2. Add Task to User")
    print("3. List All Tasks")
    print("4. Save")
    print("5. Run Slow Operation (threaded)")
    print("6. Number Stats")
    print("0. Exit")


def main():
    manager = TaskManager()

    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Enter username (leave blank for random): ").strip()
            user = manager.create_user(name or None)
            print("Created user:", user.username)

        elif choice == "2":
            user_id = input("Enter user ID: ").strip()
            title = input("Enter task title: ").strip()
            task = manager.add_task_to_user(user_id, title)
            if task:
                print("Task added:", task.title)

        elif choice == "3":
            tasks = manager.list_all_tasks()
            print("\n--- All Tasks ---")
            for t in tasks:
                status = "✔" if t.completed else "✘"
                print(f"{t.id} | {t.title} | {status}")

        elif choice == "4":
            manager.save()
            print("Data saved.")

        elif choice == "5":
            t = threaded_worker(slow_operation, 3)
            print("Slow operation started in background.")

        elif choice == "6":
            nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
            stats = calculate_statistics(nums)
            print("Stats:", stats)

        elif choice == "0":
            print("Exiting...")
            manager.save()
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()