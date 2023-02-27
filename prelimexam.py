import unittest

def multiply(x):
    return ((x - 32)*(5/9))

class converted(unittest.TestCase):

    def test(self):
        self.assertEqual(multiply(0),5)

if __name__ == '__main__':

    unittest.main()