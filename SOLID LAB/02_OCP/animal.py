# class Animal:
#     def __init__(self, species):
#         self.species = species
#
#     def get_species(self):
#         return self.species
#
#
# def animal_sound(animals: list):
#     for animal in animals:
#         if animal.species == 'cat':
#             print('meow')
#         elif animal.species == 'dog':
#             print('woof-woof')
#
#
# animals = [Animal('cat'), Animal('dog')]
# animal_sound(animals)
from abc import abstractmethod, ABC


class Animal(ABC):

    @abstractmethod
    def get_sound(self):
        pass


class Cat(Animal):
    sound = 'meow'

    def get_sound(self):
        return self.sound


class Dog(Animal):
    sound = 'woof-woof'

    def get_sound(self):
        return self.sound


class Dragon(Animal):
    sound = 'roar'

    def get_sound(self):
        return self.sound


class Donkey(Animal):
    sound = 'I am a Donkey'

    def get_sound(self):
        return self.sound


def animal_sound(animals: list):
    for animal in animals:
        print(animal.get_sound())


animals = [Dog(), Cat(), Dragon(), Donkey()]
animal_sound(animals)
# animals = [Animal('cat'), Animal('dog')]
# animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
