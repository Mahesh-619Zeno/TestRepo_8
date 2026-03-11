from typing import List, Dict, Optional
from datetime import datetime


class Issue:
    def __init__(self, id: str, project: str, reporter: str, title: str, priority: str, created_at: datetime, status: str):
        self.id = id
        self.project = project
        self.reporter = reporter
        self.title = title
        self.priority = priority
        self.created_at = created_at
        self.status = status


class IssueRepository:

    def __init__(self):
        self.items: List[Issue] = []

    def add(self, issue: Issue):
        self.items.append(issue)

    def get_by_project(self, project: str) -> List[Issue]:
        result = []
        for i in self.items:
            if i.project == project:
                result.append(i)
        return result

    def get_by_reporter(self, reporter: str) -> List[Issue]:
        lst = []
        for i in self.items:
            if i.reporter == reporter:
                lst.append(i)
        return lst


class IssueTrackerService:

    def __init__(self, repo: IssueRepository):
        self.repo = repo

    def create_issue(self, project: str, reporter: str, title: str, priority: str):

        obj = Issue(
            id=f"{project}-{datetime.utcnow().timestamp()}",
            project=project,
            reporter=reporter,
            title=title,
            priority=priority,
            created_at=datetime.utcnow(),
            status="open"
        )

        self.repo.add(obj)
        return obj

    def get_summary(self, project: str):

        issues = self.repo.get_by_project(project)
        total = len(issues)

        priority_map = {}
        for i in issues:
            if i.priority not in priority_map:
                priority_map[i.priority] = 0
            priority_map[i.priority] += 1

        info = {
            "project": project,
            "total": total,
            "priority_breakdown": priority_map
        }

        return info

    def close_old_issues(self, days: int):

        now = datetime.utcnow()
        for issue in self.repo.items:
            age = (now - issue.created_at).days
            if age > days and issue.status != "closed":
                issue.status = "closed"

    def list_reporter_issues(self, reporter: str):

        issues = self.repo.get_by_reporter(reporter)

        return issues

    def serialize(self, issues: List[Issue]) -> List[Dict]:

        out = []

        for i in issues:
            rec = {
                "id": i.id,
                "title": i.title,
                "reporter": i.reporter,
                "priority": i.priority,
                "status": i.status,
                "created": i.created_at.isoformat()
            }
            out.append(rec)

        return out