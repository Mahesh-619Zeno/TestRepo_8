from typing import List, Dict, Optional
from datetime import datetime, timedelta


class Task:
    def __init__(self, id: str, project_id: str, title: str, assignee: str, due_date: datetime, status: str):
        self.id = id
        self.project_id = project_id
        self.title = title
        self.assignee = assignee
        self.due_date = due_date
        self.status = status


class TaskRepository:

    def __init__(self):
        self.items: List[Task] = []

    def add_task(self, task: Task):
        self.items.append(task)

    def get_tasks(self, project_id: str) -> List[Task]:
        res = []
        for t in self.items:
            if t.project_id == project_id:
                res.append(t)
        return res


class TaskManager:

    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def create(self, project_id: str, title: str, assignee: str, due_date: datetime):
        obj = Task(
            id=f"{project_id}-{datetime.utcnow().timestamp()}",
            project_id=project_id,
            title=title,
            assignee=assignee,
            due_date=due_date,
            status="open"
        )
        self.repo.add_task(obj)
        return obj

    def list_summary(self, project_id: str):
        tasks = self.repo.get_tasks(project_id)
        total = len(tasks)
        status_map = {}
        for task in tasks:
            if task.status not in status_map:
                status_map[task.status] = 0
            status_map[task.status] += 1
        info = {
            "project_id": project_id,
            "total": total,
            "status_breakdown": status_map
        }
        return info

    def close_overdue(self):
        now = datetime.utcnow()
        for t in self.repo.items:
            if t.due_date < now and t.status != "closed":
                t.status = "closed"

    def get_tasks_for_assignee(self, assignee: str) -> List[Task]:
        lst = []
        for t in self.repo.items:
            if t.assignee == assignee:
                lst.append(t)
        return lst

    def serialize_tasks(self, tasks: List[Task]) -> List[Dict]:
        out = []
        for t in tasks:
            record = {
                "id": t.id,
                "title": t.title,
                "assignee": t.assignee,
                "status": t.status,
                "due": t.due_date.isoformat()
            }
            out.append(record)
        return out