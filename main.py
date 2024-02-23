from character import Character

hero = Character(name="Hero", health=100, damage=5)
enemy = Character(name="Enemy", health=60, damage=3)

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"Health of {hero.name}: {hero.health} HP.")
    print(f"Health of {enemy.name}: {enemy.health} HP.")

    input()