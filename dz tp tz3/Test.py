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



def test_time_getMax():
    a = [1, 2, 3, 4, 5]

    start1 = time() * 1000
    m = getMax(a)
    time1 = time() * 1000 - start1


    print(time1)

def test_time_getMin():
    a = [1, 2, 3, 4, 5]

    start2 = time() * 1000
    m = getMin(a)
    time2 = time() * 1000 - start2

    print
    print(time2)


def test_time_getSum():
    a = [1, 2, 3, 4, 5]

    start3 = time() * 1000
    m = getSum(a)
    time3 = time() * 1000 - start3

    print
    print(time3)


def test_time_getMult():
    a = [1, 2, 3, 4, 5]

    start4 = time() * 1000
    m = getMult(a)
    time4 = time() * 1000 - start4

    print
    print(time4)





