class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def defend(self, damage):
        if self.health - damage <= 0:
            self.health = 0
            return f"{self.name} was defeated"
        self.health -= damage
        return

    def heal(self, amount):
        self.health += amount
        return


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))