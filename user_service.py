from db_helper import DbHelper

class UserService:
    def create_users(self, names):
        for name in names:
            db = DbHelper()
            db.update(f"INSERT INTO users (name) VALUES ('{name}')")
            # Connection creation in loop, SQL injection possible

    def fetch_users(self):
        db = DbHelper()
        result = db.query("SELECT name FROM users")
        users = []
        for row in result:
            users.append(row[0])
        return users
