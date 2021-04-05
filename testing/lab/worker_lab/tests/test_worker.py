from unittest import TestCase, main

from project.worker import Worker


class WokerTests(TestCase):
    name = 'Pesho'
    salary = 1000
    energy = 10

    def setUp(self):
        self.sample_worker = Worker(self.name, self.salary, self.energy)

    def test_worker_init__when_correct_args__expect_to_init(self):
        self.assertEqual(self.name, self.sample_worker.name)
        self.assertEqual(self.salary, self.sample_worker.salary)
        self.assertEqual(self.energy, self.sample_worker.energy)

    def test_rest__when_called__expect_energy_incremented(self):
        self.sample_worker.rest()
        self.assertEqual(self.energy + 1, self.sample_worker.energy)

    def test_work__when_energy_is_0__expect_exception(self):
        self.sample_worker.energy = 0
        with self.assertRaises(Exception):
            self.sample_worker.work()

    def test_work__when_negative_energy__expect_exception(self):
        self.sample_worker.energy = -1
        with self.assertRaises(Exception):
            self.sample_worker.work()

    def test_work__when_called_positive_energy__expect_money_increased(self):
        self.sample_worker.work()
        self.sample_worker.work()
        self.assertEqual(self.salary * 2, self.sample_worker.money)

    def test_work__when_called_positive_energy__expect_energy_decreased(self):
        self.sample_worker.work()
        self.assertEqual(self.energy - 1, self.sample_worker.energy)

    def test_get_info__when_called__expect_correct_values(self):
        result = self.sample_worker.get_info()
        self.assertEqual(f'{self.name} has saved 0 money', result)


if __name__ == '__main__':
    main()

'''
Test if the worker_lab is initialized with correct name, salary and energy
Test if the worker_lab's energy is incremented after the rest method is called
Test if an error is raised if the worker_lab tries to work with negative energy or equal to 0
Test if the worker_lab's money is increased by his salary correctly after the work method is called
Test if the worker_lab's energy is decreased after the work method is called	
Test if the get_info method returns the proper string with correct values
'''

