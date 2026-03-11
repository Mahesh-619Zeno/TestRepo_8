from typing import List, Dict, Optional
from datetime import datetime, timedelta


class Session:
    def __init__(self, id: str, user_id: str, token: str, created_at: datetime, expires_at: datetime):
        self.id = id
        self.user_id = user_id
        self.token = token
        self.created_at = created_at
        self.expires_at = expires_at


class SessionRepository:

    def __init__(self):
        self.data: List[Session] = []

    def add(self, session: Session):
        self.data.append(session)

    def get_sessions(self, user_id: str) -> List[Session]:
        result = []
        for s in self.data:
            if s.user_id == user_id:
                result.append(s)
        return result


class SessionService:

    def __init__(self, repo: SessionRepository):
        self.repo = repo

    def create(self, user_id: str, token: str):

        now = datetime.utcnow()

        obj = Session(
            id=f"{user_id}-{now.timestamp()}",
            user_id=user_id,
            token=token,
            created_at=now,
            expires_at=now + timedelta(hours=2)
        )

        self.repo.add(obj)

        return obj

    def get_summary(self, user_id: str) -> Dict:

        sessions = self.repo.get_sessions(user_id)

        total = len(sessions)

        active = 0

        now = datetime.utcnow()

        for s in sessions:
            if s.expires_at > now:
                active += 1

        info = {
            "user_id": user_id,
            "total": total,
            "active": active
        }

        return info

    def remove_old(self):

        now = datetime.utcnow()

        new_list = []

        for s in self.repo.data:

            if s.expires_at > now:
                new_list.append(s)

        self.repo.data = new_list

    def transform(self, sessions: List[Session]) -> List[Dict]:

        result = []

        for s in sessions:

            record = {
                "id": s.id,
                "token": s.token,
                "created": s.created_at.isoformat(),
                "expires": s.expires_at.isoformat()
            }

            result.append(record)

        return result