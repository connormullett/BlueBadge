
import unittest


def add_two_numbers(x, y):
  return x + y


def sum_of_sums(w,x,y,z):
  a = add_two_numbers(w,x)
  b = add_two_numbers(y,z)
  return a + b


class TestDemo(unittest.TestCase):

  def test_add_two_numbers(self):
    actual = add_two_numbers(4,4)
    expected = 8
    self.assertEqual(actual, expected)

  def test_sum_of_sums(self):
      actual = sum_of_sums(4,4,4,4)
      expected = 16  
      # someone thinks that add_two_numbers
      # adds numbers together still
      self.assertEqual(actual, expected)


if __name__ == '__main__':
  y = add_two_numbers(4,4)
  print(y)

