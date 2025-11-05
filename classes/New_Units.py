from classes.Unit_abstract import AbstractUnit


class Infantry90(AbstractUnit):
    def attack(self, target: str):
        print(f"Infantry unit {self.unit_name} attacks {target} with rifles and grenades.")


class TankUnit(AbstractUnit):
    def attack(self, target: str):
        print(f"Tank unit {self.unit_name} fires heavy artillery at {target}.")


class Sniper(AbstractUnit):
    def attack(self, target: str):
        print(f"Sniper unit {self.unit_name} eliminates high-value targets at {target}.")
