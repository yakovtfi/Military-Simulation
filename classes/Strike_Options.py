class StrikeOption:
    def __init__(self, name: str, ammo: int):
        self.name = name
        self.ammo = ammo

    def strike(self, target: str = "unknown"):
        if self.ammo <= 0:
            print(f"{self.name} has no ammo left.")
            return
        self.ammo -= 1
        print(f"{self.name} strikes {target}. Ammo left: {self.ammo}")

class Tank(StrikeOption):
    def strike(self, target: str = "unknown"):
        if self.ammo <= 0:
            print(f"Tank {self.name} cannot strike; no ammo.")
            return
        self.ammo -= 1
        print(f"Tank {self.name} fires heavy shell at {target}. Ammo left: {self.ammo}")

class Drone(StrikeOption):
    def strike(self, target: str = "unknown"):
        if self.ammo <= 0:
            print(f"Drone {self.name} cannot strike; no ammo.")
            return
        self.ammo -= 1
        print(f"Drone {self.name} launches precision strike at {target}. Ammo left: {self.ammo}")