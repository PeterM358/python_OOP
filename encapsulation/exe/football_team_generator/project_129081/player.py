class Player:

    def __init__(self, name, endurance, sprint, dribble, passing, shooting):
        self.__name = name
        self.__endurance = endurance
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    def __str__(self):
        # all_props = [a for a in dir(self) if not str(a).startswith("_")]
        # print(all_props)
        # all_key_value_in_props = [f"{p.title()}: {getattr(self, p)}" for p in props]
        # print(all_key_value_in_props)

        return f"Player: {self.name}\nEndurance: {self.endurance}\n" \
               f"Sprint: {self.sprint}\nDribble: {self.dribble}\nPassing: {self.passing}\n" \
               f"Shooting: {self.shooting}\n"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def endurance(self):
        return self.__endurance

    @endurance.setter
    def endurance(self, value):
        self.__name = value

    @property
    def sprint(self):
        return self.__sprint

    @sprint.setter
    def sprint(self, value):
        self.__sprint = value

    @property
    def dribble(self):
        return self.__dribble

    @dribble.setter
    def dribble(self, value):
        self.__dribble = value

    @property
    def passing(self):
        return self.__passing

    @passing.setter
    def passing(self, value):
        self.__passing = value

    @property
    def shooting(self):
        return self.__shooting

    @shooting.setter
    def shooting(self, value):
        self.__shooting = value


# p = Player("Pall", 3, 3, 3, 3, 3)
# print(p)