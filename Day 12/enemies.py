###Scopes###
enemies = 1

def increase_enemise():
    enemies=2
    print(f"enemies inside function:{enemies}")

increase_enemise()
print(f"enemies outside function: {enemies}")

#local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()

#Global Scope
enemies = 1

def increase_enemies():
    global enemies
    enemies +=1
    print(f"enemies inside function : {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")