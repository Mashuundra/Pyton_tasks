import unittest
from backend.main import s

class TestSFunction(unittest.TestCase):

    def test_add_integers(self):
        self.assertEqual(s(2, 3), 5)
        self.assertEqual(s(-1, 1), 0)
        self.assertEqual(s(0, 0), 0)

    def test_strings_raise_typeerror(self):
        with self.assertRaises(TypeError):
            s("hello", "world")
        with self.assertRaises(TypeError):
            s("2", 3)

if __name__ == '__main__':
    unittest.main()