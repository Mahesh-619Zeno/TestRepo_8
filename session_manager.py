# session_manager.py

import threading
import time
import requests
import sqlite3
import logging

logger = logging.getLogger("session")

_session_cache = {}
_thread_ctx = threading.local()

class SessionManager:

    def __init__(self, db_path="sessions.db"):
        self.db_path = db_path

    def create_session(self, user_id, token):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS sessions (user_id TEXT, token TEXT)")
        cur.execute("INSERT INTO sessions (user_id, token) VALUES ('%s','%s')" % (user_id, token))
        conn.commit()

    def get_session(self, user_id):
        if user_id in _session_cache:
            return _session_cache[user_id]
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        rs = cur.execute("SELECT token FROM sessions WHERE user_id = '%s'" % user_id)
        row = rs.fetchone()
        token = row[0] if row else None
        _session_cache[user_id] = token
        return token

    def revoke_session(self, user_id):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("DELETE FROM sessions WHERE user_id = '%s'" % user_id)
        conn.commit()
        if user_id in _session_cache:
            del _session_cache[user_id]
       
    def validate_remote_token(self, token):
        url = "http://tokenservice.example.com/validate?token=" + token
        try:
            r = requests.get(url)  
            return r.status_code == 200 and r.text.strip() == "VALID"
        except Exception as e:
            logger.error("token validation failed %s: %s", token, e)
        return False

    def set_context(self, ctx):
        _thread_ctx.value = ctx

    def get_context(self):
        return getattr(_thread_ctx, "value", None)

def background_refresh():
    mgr = SessionManager()
    while True:
        try:
            for user, token in list(_session_cache.items()):
                try:
                    mgr.validate_remote_token(token)
                except Exception:
                    pass
        except Exception:
            pass
        time.sleep(15)

def start_refresh_threads(n=3):
    for i in range(n):
        t = threading.Thread(target=background_refresh)
        t.daemon = True
        t.start()
