from typing import List, Dict
from datetime import datetime


class Campaign:
    def __init__(self, id: str, name: str, created_at: datetime):
        self.id = id
        self.name = name
        self.created_at = created_at


class Email:
    def __init__(self, id: str, campaign_id: str, recipient: str, subject: str, sent_at: datetime):
        self.id = id
        self.campaign_id = campaign_id
        self.recipient = recipient
        self.subject = subject
        self.sent_at = sent_at


class EmailRepository:

    def __init__(self):
        self.data: List[Email] = []

    def add(self, email: Email):
        self.data.append(email)

    def get_by_campaign(self, campaign_id: str) -> List[Email]:
        result = []

        for e in self.data:
            if e.campaign_id == campaign_id:
                result.append(e)

        return result


class CampaignService:

    def __init__(self, repo: EmailRepository):
        self.repo = repo

    def send(self, campaign_id: str, recipient: str, subject: str):

        obj = Email(
            id=f"{campaign_id}-{datetime.utcnow().timestamp()}",
            campaign_id=campaign_id,
            recipient=recipient,
            subject=subject,
            sent_at=datetime.utcnow()
        )

        self.repo.add(obj)

        return obj

    def get_report(self, campaign_id: str) -> Dict:

        emails = self.repo.get_by_campaign(campaign_id)

        total = len(emails)

        domain_map = {}

        for email in emails:

            domain = email.recipient.split("@")[-1]

            if domain not in domain_map:
                domain_map[domain] = 0

            domain_map[domain] += 1

        data = {
            "campaign_id": campaign_id,
            "total": total,
            "domains": domain_map
        }

        return data

    def clean_old(self, days: int):

        now = datetime.utcnow()

        new_items = []

        for e in self.repo.data:

            diff = (now - e.sent_at).days

            if diff <= days:
                new_items.append(e)

        self.repo.data = new_items

    def format(self, emails: List[Email]) -> List[Dict]:

        out = []

        for e in emails:

            record = {
                "id": e.id,
                "recipient": e.recipient,
                "subject": e.subject,
                "sent": e.sent_at.isoformat()
            }

            out.append(record)

        return out