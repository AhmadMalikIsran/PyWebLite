import uuid

def generate_unique_session_id():
    return str(uuid.uuid4())

class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, user_id):
        session_id = generate_unique_session_id()
        self.sessions[session_id] = user_id
        return session_id

    def get_user_id(self, session_id):
        return self.sessions.get(session_id)
