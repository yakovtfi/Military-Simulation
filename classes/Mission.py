from classes.Agent import Agent
from classes.Unit_abstract import AbstractUnit

class Mission:
    def __init__(self, mission_name: str, target: str, assigned_agent: Agent, involved_units: list[AbstractUnit]):

        self.mission_name = mission_name
        self.target = target
        self.assigned_agent = assigned_agent
        self.involved_units = involved_units

    def briefing(self):
        print(f"\nMission: {self.mission_name}")
        print(f"Target: {self.target}")
        print(f"Assigned Agent: {self.assigned_agent.codename}")
        print("Involved Units:")
        for unit in self.involved_units:
            print(f" - {unit.unit_name}")

