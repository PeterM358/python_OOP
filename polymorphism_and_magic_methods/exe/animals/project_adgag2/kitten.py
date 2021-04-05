from project.cat import Cat


class Kitten(Cat):

    def __init__(self, name, age, gender='Female'):
        self.gender = gender
        super().__init__(name, age, gender)

    def make_sound(self):
        return 'Meow'


# kiti = Kitten('kiti', 1)
# print(kiti)