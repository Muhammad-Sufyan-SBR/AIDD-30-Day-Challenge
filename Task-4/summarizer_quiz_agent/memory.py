from persistence import load_session, save_session, clear_session

class AgentMemory:
    """
    Wrapper class for agent memory management, compliant with 
    Context7/OpenAgents architectural patterns.
    """
    def __init__(self):
        self.data = load_session()

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
        self.commit()

    def update(self, new_data: dict):
        self.data.update(new_data)
        self.commit()

    def commit(self):
        save_session(self.data)

    def clear(self):
        self.data = {}
        clear_session()
