from unittest import TestCase, main

from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware


class TestHardware(TestCase):
    def setUp(self) -> None:
        self.hardware = Hardware('HDD', 'Heavy', 1000, 1000)

    def test_init_expect_correct_attrs(self):
        self.assertEqual('HDD', self.hardware.name)
        self.assertEqual('Heavy', self.hardware.type)
        self.assertEqual(1000, self.hardware.capacity)
        self.assertEqual(1000, self.hardware.memory)
        self.assertEqual([], self.hardware.software_components)

    def test_install__when_max_capacity_and_memory_usage__expect_installed(self):
        software = ExpressSoftware('Linux', 1000, 500)
        self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))

    def test_install__when_low_capacity__expect_exception(self):
        software = ExpressSoftware('Linux', 1001, 500)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)
        self.assertEqual('Software cannot be installed', str(ex.exception))

    def test_install__when_low_memory__expect_exception(self):
        software = ExpressSoftware('Linux', 1000, 501)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)
        self.assertEqual('Software cannot be installed', str(ex.exception))

    def test_uninstall__when_software_in_list__expect_software_removerd(self):
        software = ExpressSoftware('Linux', 200, 200)
        self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))
        self.hardware.uninstall(software)
        self.assertEqual(0, len(self.hardware.software_components))

    def test_uninstall__when_invalid_software__expect_NONE(self):
        software = ExpressSoftware('Linux', 200, 200)
        software2 = ExpressSoftware('Linux', 1, 1)
        self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))
        self.assertIsNone(self.hardware.uninstall(software2))
        self.assertEqual(1, len(self.hardware.software_components))


if __name__ == '__main__':
    main()