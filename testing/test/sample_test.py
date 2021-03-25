import unittest
from unittest import mock

from app.utils import Utils


class SampleTests(unittest.TestCase):
    # when_ints__utils_sum__expect_correct (pure 3A)
    # act__arrange__assert
    # assert arrange act

    # test_utilsSum_whenInts_expectCorrect
    @mock.patch('app.validators.TypeValidator')
    def test_utils_sum__when_ints__expect_correct_result(self, validator_mock):
        # Arrange (prepare)
        ValidatorMock = validator_mock.return_value
        ValidatorMock.validate.return_value = None
        utils = Utils()
        numbers = [1, 2, 3, 4]

        # Act
        actual_result = utils.sum(numbers)

        # Assert
        expected_result = 10.1
        self.assertEqual(expected_result, actual_result, 'Actual result is not equal to expected')

    def test_my_sum__when_floats__expect_to_be_equal(self):
        numbers = [1.0, 2.0, 3.0, 4.0]
        utils = Utils()
        actual_result = utils.sum(numbers)
        expected_result = 10.0

        self.assertEqual(expected_result, actual_result)

    def test_my_sum__when_strings__expect_value_exception(self):
        numbers = ['a', 'b', 'c']
        utils = Utils()
        with self.assertRaises(ValueError) as context:
            utils.my_sum(numbers)


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
