from character import Hero, Enemy
from weapon import *

def space():
    print()

# Small welcome screen
print("Type 'exit' or 'q' to quit.")
space()

# Hero properties
hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)

space()

# Enemy properties
enemy = Enemy(name="Enemy", health=60, weapon=short_bow)

while True:
    print("-" * 6, "Damage Indicator", "-" * 6)
    hero.attack(enemy)
    enemy.attack(hero)

    space()

    print("-" * 6, "Stats", "-" * 6)
    print(f"Health of {hero.name}: {hero.health} HP.")
    print(f"Health of {enemy.name}: {enemy.health} HP.")

    inp = input()

    if inp == "exit" or inp == "q":
        break