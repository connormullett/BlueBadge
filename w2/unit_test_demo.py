
import unittest


def add_two_numbers(x, y):
  return x + y


class TestDemo(unittest.TestCase):

    def test_add_two_numbers(self):
      actual = add_two_numbers(4,4)
      expected = 8
      self.assertEqual(actual, expected)


if __name__ == '__main__':
  y = add_two_numbers(4,4)
  print(y)

