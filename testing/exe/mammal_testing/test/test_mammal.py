from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    name = 'Molly'
    type = 'Dog'
    sound = 'woof woof'

    def setUp(self):
        self.my_dog = Mammal(self.name, self.type, self.sound)

    def test_make_sound(self):
        self.assertEqual(f'Molly makes woof woof', self.my_dog.make_sound())

    def test_get_kingdom(self):
        self.assertEqual('animals', self.my_dog.get_kingdom())

    def test_info(self):
        self.assertEqual("Molly is of type Dog", self.my_dog.info())

    def test_init(self):
        self.assertEqual(self.name, self.my_dog.name)
        self.assertEqual(self.type, self.my_dog.type)
        self.assertEqual(self.sound, self.my_dog.sound)


if __name__ == '__main__':
    main()
