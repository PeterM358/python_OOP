from unittest import TestCase, main

# from project.cat import Cat


class CatTests(TestCase):
    name = 'Kitty'

    def setUp(self):
        self.cat = Cat('Kitty')

    def test_eat__when_called__expect_size_increased(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_eat__when_called__expect_cat_fed(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_eat__when_cat_is_fed__expect_exception(self):
        self.cat.eat()
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_sleep__when_cat_not_fed__expect_exception_not_fed(self):
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_sleep__when_called__expect_cat_not_sleepy(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()