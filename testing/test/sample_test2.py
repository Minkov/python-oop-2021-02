import unittest

from app.utils import my_sum


class SampleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('SetUpClass')

    @classmethod
    def tearDownClass(cls):
        print('TearDownClass')

    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_my_sum__when_ints__expect_to_be_equal(self):
        numbers = [1, 2, 3, 4]
        actual_result = my_sum(numbers)
        expected_result = 10

        self.assertEqual(expected_result, actual_result)

    def test_my_sum__when_floats__expect_to_be_equal(self):
        numbers = [1.0, 2.0, 3.0, 4.0]
        actual_result = my_sum(numbers)
        expected_result = 10

        self.assertEqual(expected_result, actual_result)

    def test_my_sum__when_strings__expect_value_exception(self):
        numbers = ['a', 'b', 'c']
        with self.assertRaises(ValueError) as context:
            my_sum(numbers)

        expected_message = '`numbers` should be ints or floats'
        actual_message = context.exception.args[0]

        self.assertEqual(expected_message, actual_message)


class SampleTests2(unittest.TestCase):
    def test_my_sum__when_ints__expect_to_be_equal(self):
        numbers = [1, 2, 3, 4]
        actual_result = my_sum(numbers)
        expected_result = 10

        self.assertEqual(expected_result, actual_result)

    def test_my_sum__when_floats__expect_to_be_equal(self):
        numbers = [1.0, 2.0, 3.0, 4.0]
        actual_result = my_sum(numbers)
        expected_result = 10.0

        self.assertEqual(expected_result, actual_result)

    def test_my_sum__when_strings__expect_value_exception(self):
        numbers = ['a', 'b', 'c']
        with self.assertRaises(ValueError) as context:
            my_sum(numbers)
