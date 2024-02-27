import random
class Weapon:
    def __init__(self, 
                 name: str, 
                 weapon_type: str, 
                 damage: int, 
                 value: int) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value

    def update_damage(self) -> None:
        if self.name == "Iron Sword":
            self.damage = random.randint(1, 5)

        elif self.name == "Short Bow":
            self.damage = random.randint(2, 4)

        else:
            self.damage = random.randint(0, 2)

iron_sword = Weapon(name="Iron Sword", 
                    weapon_type="sharp", 
                    damage=random.randint(1, 5), 
                    value=10)

short_bow = Weapon(name="Short Bow",
                   weapon_type="ranged",
                   damage=random.randint(2, 4),
                   value=8)

fists = Weapon(name="Fists",
               weapon_type="blunt",
               damage=random.randint(0, 2),
               value=0)

# Update the damage
def dmg_update():
    iron_sword.update_damage()
    short_bow.update_damage()
    fists.update_damage()