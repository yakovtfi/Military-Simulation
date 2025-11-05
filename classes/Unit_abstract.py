from abc import ABC, abstractmethod
from typing import List, Optional
from classes.Soldier import Soldier
from classes.Strike_Options import StrikeOption

class AbstractUnit(ABC):
    def __init__(self, unit_name: str, commander: Soldier, soldiers: List[Soldier]):
        self.unit_name = unit_name
        self.commander = commander
        self.soldiers = soldiers

    @abstractmethod
    def attack(self, target: str):
        pass

    def briefing(self):
        print(f"Unit: {self.unit_name}")
        print("Commander Report:")
        self.commander.report()
        print("\nSoldiers in Unit:")
        for soldier in self.soldiers:
            soldier.report()

class Unit(AbstractUnit):
    def __init__(self, unit_name: str, commander: Soldier, soldiers: List[Soldier], strike_options: Optional[List[StrikeOption]] = None):
        super().__init__(unit_name, commander, soldiers)
        self.strike_options = strike_options or []

    def attack(self, target: str):
        if not self.strike_options:
            print(f"{self.unit_name} has no strike options to attack {target}.")
            return
        for option in self.strike_options:
            option.strike(target)

    def strike_all(self, target: str):
        self.attack(target)

class Infantry(AbstractUnit):
    def attack(self, target: str):
        print(f"Infantry unit {self.unit_name} attacks {target} with rifles and grenades.")

class TankUnit(AbstractUnit):
    def attack(self, target: str):
        print(f"Tank unit {self.unit_name} fires heavy artillery at {target}.")

class Sniper(AbstractUnit):
    def attack(self, target: str):
        print(f"Sniper unit {self.unit_name} eliminates high-value targets at {target}.")