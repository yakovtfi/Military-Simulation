from classes.Army_Inventory import Weapon

class Soldier:
    def __init__(self, name: str, rank: str, weapon: Weapon):
        self.name = name
        self.rank = rank
        self.weapon = weapon

    def report(self):
        print(f"Soldier: {self.rank} {self.name} | {self.weapon}")


