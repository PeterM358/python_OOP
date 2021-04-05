from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.main_hero = Hero('Goku', 2, 100, 10)
        self.enemy_hero = Hero('Freizer', 1, 80, 5)

    def test_init(self):
        self.assertEqual('Goku', self.main_hero.username)
        self.assertEqual(2, self.main_hero.level)
        self.assertEqual(100, self.main_hero.health)
        self.assertEqual(10, self.main_hero.damage)

    def test_battle__when_attack_same_hero__expect_exception(self):
        hero_self = Hero('Goku', 6, 80, 60)
        with self.assertRaises(Exception) as ex:
            self.main_hero.battle(hero_self)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle__when_self_health_is_0__expect_exception(self):
        self.main_hero.health = 0
        self.assertEqual(0, self.main_hero.health)
        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.enemy_hero)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest',
                         str(ex.exception))

    def test_battle__when_self_health_is_negative__expect_exception(self):
        self.main_hero.health = -1
        self.assertEqual(-1, self.main_hero.health)
        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.enemy_hero)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest',
                         str(ex.exception))

    def test_battle__when_enemy_health_is_0__expect_exception(self):
        self.enemy_hero.health = 0
        self.assertEqual(0, self.enemy_hero.health)
        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.enemy_hero)
        self.assertEqual('You cannot fight Freizer. He needs to rest',
                         str(ex.exception))

    def test_battle__when_enemy_health_is_negative__expect_exception(self):
        self.enemy_hero.health = -1
        self.assertEqual(-1, self.enemy_hero.health)
        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.enemy_hero)
        self.assertEqual('You cannot fight Freizer. He needs to rest',
                         str(ex.exception))

    def test_battle__when_both_heroes_health_below_or_0__expect_exception(self):
        self.main_hero.damage = 40
        self.enemy_hero.damage = 110

        result = self.main_hero.battle(self.enemy_hero)
        self.assertEqual('Draw', result)

    def test_battle__when_main_hero_wins_battle__expect_main_hero_attrs_increase(self):
        self.main_hero.damage = 41

        result = self.main_hero.battle(self.enemy_hero)
        self.assertEqual('You win', result)
        self.assertEqual(3, self.main_hero.level)
        self.assertEqual(100, self.main_hero.health)
        self.assertEqual(46, self.main_hero.damage)
        self.assertTrue(self.enemy_hero.health <= 0)

    def test_battle__when_enemy_hero_wins_battle__expect_enemy_hero_attrs_increase(self):
        self.enemy_hero.damage = 101

        result = self.main_hero.battle(self.enemy_hero)
        self.assertEqual('You lose', result)
        self.assertEqual(2, self.enemy_hero.level)
        self.assertEqual(65, self.enemy_hero.health)
        self.assertEqual(106, self.enemy_hero.damage)
        self.assertTrue(self.main_hero.health <= 0)

    def test_str_represent__when_called__expect_correct_data(self):
        self.assertEqual("Hero Goku: 2 lvl\nHealth: 100\nDamage: 10\n",
                         str(self.main_hero))


if __name__ == '__main__':
    main()