class Agent:

    def __init__(self, code_name: str, real_name: str, location: str, status: str, missions_completed: int, id: int= 0):
        self.code_name = code_name
        self.real_name = real_name
        self.location = location
        self.status = status
        self.missions_completed = missions_completed
        self.id = id


    def __str__(self):
        return (f"agent id: {self.id}, name: {self.real_name}, code name: {self.code_name},"
                f"location: {self.location}, status: {self.status},"
                f" num missions completed: {self.missions_completed}")