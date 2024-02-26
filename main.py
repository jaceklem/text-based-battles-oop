from character import Hero, Enemy
from weapon import *

def space():
    """Function that inputs a space between two lines
    """
    print()

### WEAPON SELECTION ###
#    iron_sword
#    short_bow
#    fists

# Small welcome screen
print("Type 'exit' or 'q' to quit.")
space()

# Hero properties
hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)

# Enemy properties
enemy = Enemy(name="Enemy", health=60, weapon=short_bow)

while True:
    space()
    print("-" * 6, "Damage Indicator", "-" * 6)

    hero.attack(enemy)
    enemy.attack(hero)

    space()

    print("-" * 6, "Stats", "-" * 6)
    hero.health_bar.draw()
    enemy.health_bar.draw()

    inp = input()

    if inp.lower() == "swap":
        hero.drop()

        new_weapon = input("Choose your new weapon: ")
        space()

        if new_weapon.lower() == "sword":
            hero.equip(iron_sword)
            continue

        if new_weapon.lower() == "bow":
            hero.equip(short_bow)
            continue

        if new_weapon.lower() == "":
            hero.equip(fists)
            continue

    if inp.lower() == "exit" or inp.lower() == "q":
        break
