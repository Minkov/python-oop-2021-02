import unittest

from lab_resources.cat.cat import Cat


class CatTests(unittest.TestCase):
    name = 'Kitty'

    def setUp(self):
        self.cat = Cat(self.name)

    def test_cat_eat__expect_size_to_be_increased_by_1(self):
        """Cat's size is increased after eating"""
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_cat_eat__expect_fed_to_be_true(self):
        """Cat is fed after eating"""
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_sleep__when_fed__expect_not_to_be_sleepy(self):
        """Cat is not sleepy after sleeping"""
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

    def test_cat_eat__when_fed__expect_exception(self):
        """Cat cannot eat if already fed, raises an error"""
        self.cat.eat()

        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat_sleep__when_not_fed__expect_exception(self):
        """Cat cannot fall asleep if not fed, raises an error"""
        with self.assertRaises(Exception):
            self.cat.sleep()

if __name__ == '__main__':
    unittest.main()
