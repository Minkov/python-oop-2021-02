import unittest


class TestWorker(unittest.TestCase):
    name = 'Test Worker'
    salary = 1000
    energy = 3

    def setUp(self):
        self.worker = Worker(self.name, self.salary, self.energy)

    def test_worker_init__when_correct_args__expect_to_be_initialized(self):
        """Test if the worker is initialized with correct name, salary and energy"""
        self.assertEqual(self.name, self.worker.name)
        self.assertEqual(self.salary, self.worker.salary)
        self.assertEqual(self.energy, self.worker.energy)

    def test_worker_rest___expect_energy_to_be_incremented(self):
        """Test if the worker's energy is incremented after the rest method is called"""
        self.worker.rest()
        self.assertEqual(self.energy + 1, self.worker.energy)

    def test_worker_work__when_energy_is_0_expect_exception(self):
        """Test if an error is raised if the worker tries to work with negative energy or equal to 0"""
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_work__when_energy_is_above_0_expect_money_to_be_increased_by_salary(self):
        """Test if the worker's money is increased by his salary correctly after the work method is called"""
        self.worker.work()
        self.worker.work()
        self.assertEqual(self.salary * 2, self.worker.money)

    def test_worker_work__when_energy_is_above_0_expect_energy_to_be_decremented(self):
        """Test if the worker's energy is decreased after the work method is called"""
        self.worker.work()
        self.assertEqual(self.energy - 1, self.worker.energy)

    def test_worker_get_info__expect_correct_values(self):
        """Test if the get_info method returns the proper string with correct values"""
        expected_info = f'{self.name} has saved 0 money.'
        actual_info = self.worker.get_info()
        self.assertEqual(expected_info, actual_info)


if __name__ == '__main__':
    unittest.main()
