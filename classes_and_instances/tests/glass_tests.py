import unittest

from lab.glass import Glass


class Tests(unittest.TestCase):
    def test_init(self):
        glass = Glass()
        self.assertEqual(glass.content, 0)
        self.assertEqual(Glass.capacity, 250)

    def test_fill_successfull(self):
        glass = Glass()
        res = glass.fill(100)
        self.assertEqual(res, "Glass filled with 100 ml")
        self.assertEqual(glass.content, 100)

    def test_fill_unsuccessfull(self):
        glass = Glass()
        res = glass.fill(251)
        self.assertEqual(res, "Cannot add 251 ml")
        self.assertEqual(glass.content, 0)

    def test_empty(self):
        glass = Glass()
        glass.fill(150)
        res = glass.empty()
        self.assertEqual(res, "Glass is now empty")
        self.assertEqual(glass.content, 0)

    def test_info(self):
        glass = Glass()
        glass.fill(50)
        res = glass.info()
        self.assertEqual(res, "200 ml left")


if __name__ == "__main__":
    unittest.main()
