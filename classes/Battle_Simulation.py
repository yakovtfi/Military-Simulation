from typing import List
from classes.Unit_abstract import AbstractUnit


class Army:
    total_attacks = 0

    def __init__(self, name: str, units: List[AbstractUnit] = None):
        self.name = name
        self.units = units or []

    def add_unit(self, unit: AbstractUnit):
        self.units.append(unit)

    def attack_all(self, target: str):
        if not self.units:
            print(f"{self.name} has no units.")
            return
        print(f"\nArmy '{self.name}' commencing coordinated attack on {target}.\n")
        for unit in self.units:
            unit.attack(target)
            Army.total_attacks += 1
        print(f"\nArmy '{self.name}' completed coordinated attack on {target}.")
