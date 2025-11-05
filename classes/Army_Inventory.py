class Weapon:
    total_weapons = 0

    def __init__(self, name: str, ammo: int):
        self.name = name
        self.ammo = ammo
        Weapon.total_weapons += 1

    def __str__(self):
        return f"Weapon: {self.name}, Ammo: {self.ammo}"


