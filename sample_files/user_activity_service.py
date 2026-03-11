from typing import List, Dict
from datetime import datetime


class Activity:
    def __init__(self, id: str, user_id: str, action: str, created_at: datetime):
        self.id = id
        self.user_id = user_id
        self.action = action
        self.created_at = created_at


class ActivityRepository:

    def __init__(self):
        self.data: List[Activity] = []

    def add(self, activity: Activity):
        self.data.append(activity)

    def get_user_activities(self, user_id: str) -> List[Activity]:
        items = []

        for act in self.data:
            if act.user_id == user_id:
                items.append(act)

        return items


class UserActivityService:

    def __init__(self, repo: ActivityRepository):
        self.repo = repo

    def process_activity(self, user_id: str, action: str):

        obj = Activity(
            id=f"{user_id}-{datetime.utcnow().timestamp()}",
            user_id=user_id,
            action=action,
            created_at=datetime.utcnow()
        )

        self.repo.add(obj)

        return obj

    def get_activity_summary(self, user_id: str) -> Dict:

        data = self.repo.get_user_activities(user_id)

        total = len(data)

        action_map = {}

        for item in data:

            if item.action not in action_map:
                action_map[item.action] = 0

            action_map[item.action] += 1

        result = {
            "user_id": user_id,
            "total": total,
            "actions": action_map
        }

        return result

    def clean_old(self, days: int):

        now = datetime.utcnow()

        new_list = []

        for a in self.repo.data:

            diff = (now - a.created_at).days

            if diff <= days:
                new_list.append(a)

        self.repo.data = new_list

    def transform(self, activities: List[Activity]) -> List[Dict]:

        res = []

        for a in activities:
            obj = {
                "id": a.id,
                "action": a.action,
                "time": a.created_at.isoformat()
            }

            res.append(obj)

        return res