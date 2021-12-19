from time import time
from main import getSum, getMult, getMax, getMin


def test_Max():
    a = [1, 2, 3, 4, 5]
    assert getMax(a) == 5

def test_Min():
    a = [1, 2, 3, 4, 5]
    assert getMin(a) == 1

def test_Sum():
    a = [1, 2, 3, 4, 5]
    assert getSum(a) == 15

def test_Mult():
    a = [1, 2, 3, 4, 5]
    assert getMult(a) == 120
