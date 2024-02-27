from character import Hero, Enemy
from weapon import *

def space():
    """Function that inputs a space between two lines
    """
    print()

def help():
    print('-' * 6, 'HELP OPTIONS', '-' * 6)
    print("Type 'swap' to switch weapons.")
    print("Type 'regen' to regenerate health.") 

### WEAPON SELECTION ###
#    iron_sword
#    short_bow
#    fists

# Small welcome screen
print("-" * 6, "Welcome to Text-based Battles", "-" * 6)
print("Type 'help' for options.")
print("Type 'a' to attack")
print("Type 'exit' or 'q' to quit.")
space()

# Hero properties
hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)

# Enemy properties
enemy = Enemy(name="Enemy", health=75, weapon=short_bow)

while True:
    print("-" * 6, "Stats", "-" * 6)
    hero.health_bar.draw()
    enemy.health_bar.draw()

    space()

    print("-" * 6, "Your Turn", "-" * 6)
    inp = input("Action: ")

    space()

    if inp.lower() == 'a' or inp.lower() == 'attack':
        print("-" * 6, "Damage Indicator", "-" * 6)

        dmg_update()

        hero.attack(enemy)
        enemy.attack(hero)
        space()

    if inp.lower() == "swap":
        hero.drop()
        space()

        print("Choose from 'sword', 'bow', '[ENTER]'.")
        new_weapon = input("Choose your new weapon: ")
        space()

        if new_weapon.lower() == "sword":
            hero.equip(iron_sword)

        if new_weapon.lower() == "bow":
            hero.equip(short_bow)

        if new_weapon.lower() == "":
            hero.equip(fists)

    if inp.lower() == "regen":
        hero.healing()
        space()

    if inp.lower() == 'help':
        help()
        space()

    if hero.health == 0:
        print('The enemy has won!')
        break
    
    if enemy.health == 0:
        print('The hero has won!!')
        break

    if inp.lower() == "exit" or inp.lower() == "q":
        break