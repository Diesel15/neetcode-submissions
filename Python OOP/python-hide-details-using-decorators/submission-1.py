class SuperHero:
    def __init__(self, name: str, health: int, power_level: int):
        self.name = name
        self.__health = health
        self.__power_level = power_level

    @property
    def health(self) -> int:
        return self.__health

    @property
    def power_level(self) -> int:
        return self.__power_level

    @health.setter
    def health(self, val: int) -> None:
        if val > 100:
            print("You can't set the health to more than 100")
        elif val < 0:
            print("You can't set the health to less than 0")
        else:
            self.__health = val

    @power_level.setter
    def power_level(self, val:int) -> None:
        if val > 10:
            print("You can't set the power level to more than 10")
        elif val < 1:
            print("You can't set the power level to less than 1")
        else:
            self.__power_level = val


super_hero = SuperHero("Batman", 80, 9)

print(super_hero.health) 
super_hero.health = 110 

print(super_hero.power_level)
super_hero.power_level = 100 
super_hero.power_level = 0 

print(f"{super_hero.name} has {super_hero.health} health and {super_hero.power_level} power level")