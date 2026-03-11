from typing import List, Dict
from datetime import datetime


class Document:
    def __init__(self, id: str, owner_id: str, file_name: str, created_at: datetime):
        self.id = id
        self.owner_id = owner_id
        self.file_name = file_name
        self.created_at = created_at


class DocumentRepository:

    def __init__(self):
        self.records: List[Document] = []

    def save(self, doc: Document):
        self.records.append(doc)

    def get_documents(self, owner_id: str) -> List[Document]:
        result = []

        for r in self.records:
            if r.owner_id == owner_id:
                result.append(r)

        return result


class DocumentProcessingService:

    def __init__(self, repo: DocumentRepository):
        self.repo = repo

    def process(self, owner_id: str, file_name: str):

        obj = Document(
            id=f"{owner_id}-{datetime.utcnow().timestamp()}",
            owner_id=owner_id,
            file_name=file_name,
            created_at=datetime.utcnow()
        )

        self.repo.save(obj)

        return obj

    def generate_stats(self, owner_id: str) -> Dict:

        docs = self.repo.get_documents(owner_id)

        total = len(docs)

        type_map = {}

        for d in docs:

            ext = d.file_name.split(".")[-1]

            if ext not in type_map:
                type_map[ext] = 0

            type_map[ext] += 1

        data = {
            "owner_id": owner_id,
            "total": total,
            "types": type_map
        }

        return data

    def remove_old(self, days: int):

        now = datetime.utcnow()

        new_data = []

        for doc in self.repo.records:

            diff = (now - doc.created_at).days

            if diff <= days:
                new_data.append(doc)

        self.repo.records = new_data

    def transform(self, docs: List[Document]) -> List[Dict]:

        out = []

        for doc in docs:
            rec = {
                "id": doc.id,
                "file": doc.file_name,
                "time": doc.created_at.isoformat()
            }

            out.append(rec)

        return out