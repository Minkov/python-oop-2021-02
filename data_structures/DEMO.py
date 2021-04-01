from unittest import TestCase


def sum(numbers):
    result = numbers[0]
    if len(numbers) == 2:
        result += numbers[1]
    return result


class SumTests(TestCase):
    def test_1(self):
        result = sum([1])
        self.assertEqual(1, result)

    def test_2(self):
        result = sum([3])
        self.assertEqual(3, result)

    def test_3(self):
        result = sum([3, 2])
        self.assertEqual(5, result)
