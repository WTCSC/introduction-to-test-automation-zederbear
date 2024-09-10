import pytest
import math_it_up

"""
This file contains the tests for the math_it_up module, which contains the
following functions:

- math_it_up.is_even
- math_it_up.is_odd
- math_it_up.mean
- math_it_up.median
- math_it_up.mode

The `is_even` and `is_odd` functions accept a single argument, a number, and
return True if the number is even or odd, respectively.

The `mean` function accepts a single argument, a list of numbers, and returns
the mean of the numbers.

The `median` function accepts a single argument, a list of numbers, and returns
the median of the numbers.

The `mode` function accepts a single argument, a list of numbers, and returns
the mode of the numbers.

To run the tests, run `pytest` from the command line in the same directory as
this file.
"""

def test_is_even():
  """
  Tests for the `is_even` function
  """
  assert math_it_up.is_even(1) == False
  assert math_it_up.is_even(2) == True
  assert math_it_up.is_even(12341412) == True
  assert math_it_up.is_even(58493) == False

def test_is_odd():
  """
  Tests for the `is_odd` function
  """
  assert math_it_up.is_odd(1) == True
  assert math_it_up.is_odd(2) == False
  assert math_it_up.is_odd(12341412) == False
  assert math_it_up.is_odd(58493) == True

def test_mean():
  """
  Tests for the `mean` function
  """
  assert math_it_up.mean([1, 2, 3]) == 2
  assert math_it_up.mean([20, 40, 60]) == 40
  assert math_it_up.mean([1, 55, 23, 72, 33, 324]) == 84.66666666666667

def test_median():
  """
  Tests for the `median` function
  """
  assert math_it_up.median([1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 7, 6, 5, 6]) == 6
  assert math_it_up.median([2, 3, 6, 4, 3, 7 ,13, 4,5, 6]) == 4.5

def test_mode():
  """
  Tests for the `mode` function
  """
  assert math_it_up.mode([1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 7, 6, 5, 6]) == [6]
  assert math_it_up.mode([2, 3, 6, 4, 3, 7 ,13, 4,5, 6]) == [3, 6, 4]