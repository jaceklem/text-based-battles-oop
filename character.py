class Character:
    def __init__(self, name: str, health: int, damage: int):
        self.name = name
        self.health = health
        self.health_max = health
        self.damage = damage

    def attack(self, target):
        target.hp -= self.damage
        target.hp = max(target.hp, 0)