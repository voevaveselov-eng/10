import math_functions
#test 2
def test_add(): assert math_functions.add(2, 3) == 5
def test_subtract(): assert math_functions.subtract(10, 4) == 6
def test_multiply(): assert math_functions.multiply(3, 7) == 21
def test_divide(): assert math_functions.divide(20, 4) == 5
def test_divide_by_zero(): assert math_functions.divide(10, 0) == 0
#https://github.com/voevaveselov-eng/10.git