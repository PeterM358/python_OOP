from unittest import TestCase, main

from project.rooms.room import Room


class TestRoom(TestCase):
    name = 'Kokis'
    budget = 10
    members = 4

    def setUp(self):
        self.room = Room(self.name, self.budget, self.members)

    def test_init__when_valid__expect_attrs_set(self):

        self.assertEqual(self.name, self.room.family_name)
        self.assertEqual(self.budget, self.room.budget)
        self.assertEqual(self.members, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)
        for attr in ['family_name', 'budget', 'members_count', 'children', 'expenses']:
            self.assertTrue(hasattr(self.room, attr))

    def test_expenses__when_0__expect_expenses(self):
        self.room.expenses = 0
        self.assertEqual(0, self.room.expenses)

    def test_expenses__when_positive__expect_expenses(self):
        self.room.expenses = 1
        self.assertEqual(1, self.room.expenses)

    def test_expenses__when_negative__expect_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -1
        self.assertEqual('Expenses cannot be negative', str(ex.exception))


if __name__ == '__main__':
    main()
