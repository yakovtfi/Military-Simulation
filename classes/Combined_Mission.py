from classes.Soldier import Soldier
from classes.Mission import Mission

class Commander(Soldier):
    def __init__(self, name: str, rank: str, weapon):
        super().__init__(name, rank, weapon)
        self.rank_level = 10



class ReconMission(Mission):
    def execute(self):
        print(f"\nExecuting Recon Mission: {self.mission_name}")
        for unit in self.involved_units:
            print(f"Recon by {unit.unit_name} on target: {self.target}")

class StrikeMission(Mission):
    def execute(self):
        print(f"\nExecuting Strike Mission: {self.mission_name}")
        for unit in self.involved_units:
            unit.attack(self.target)

class RescueMission(Mission):
    def execute(self):
        print(f"\nExecuting Rescue Mission: {self.mission_name}")
        for unit in self.involved_units:
            print(f"{unit.unit_name} performs rescue operation at {self.target}")