from project.cat import Cat


class Tomcat(Cat):

    def __init__(self, name, age, gender='Male'):
        self.gender = gender
        super().__init__(name, age, gender)

    def make_sound(self):
        return 'Hiss'