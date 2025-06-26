class Agent:

    def __init__(self, code_name: str, real_name: str, location: str, status: str, missions_completed: int, id: int= 0):
        self.code_name = code_name
        self.real_name = real_name
        self.location = location
        self.status = status
        self.missions_completed = missions_completed
        self.id = id