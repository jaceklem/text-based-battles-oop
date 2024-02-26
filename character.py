from weapon import *
from health_bar import HealthBar

class Character:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
        self.health_max = health

        self.weapon = fists

    def attack(self, target):
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()

        print(f"{self.name} dealt {self.weapon.damage} damage to {target.name} using {self.weapon.name}")


class Hero(Character):
    def __init__(self, name: str, health: int):
        super().__init__(name=name, health=health)
        
        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, color='green')

    def equip(self, weapon: str) -> None:
        self.weapon = weapon

        print(f"{self.name} equipped a(n) {self.weapon.name}")

    def drop(self) -> None:
        print(f"{self.name} dropped {self.weapon}!")

        self.weapon = self.default_weapon



class Enemy(Character):
    def __init__(self, name: str, health: int, weapon: str) -> None:
        super().__init__(name=name, health=health)

        self.weapon = weapon
        self.health_bar = HealthBar(self, color='red')