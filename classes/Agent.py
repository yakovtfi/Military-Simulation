class Agent:
    def __init__(self, codename: str, clearance_level: int):
        self.codename = codename
        self.clearance_level = clearance_level

    def __str__(self):
        return f"Agent {self.codename} (Clearance: {self.clearance_level})"



