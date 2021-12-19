from time import time
from main import getSum, getMult, getMax, getMin


def time_getMax():
    a = [1, 2, 3, 4, 5]

    start1 = time() * 1000
    m = getMax(a)
    time1 = time() * 1000 - start1
    return time1




def time_getMin():
    a = [1, 2, 3, 4, 5]

    start2 = time() * 1000
    m = getMin(a)
    time2 = time() * 1000 - start2
    return time2




def time_getSum():
    a = [1, 2, 3, 4, 5]

    start3 = time() * 1000
    m = getSum(a)
    time3 = time() * 1000 - start3
    return time3


def time_getMult():
    a = [1, 2, 3, 4, 5]

    start4 = time() * 1000
    m = getMult(a)
    time4 = time() * 1000 - start4
    return time4


f = open("test.txt", "w")
f.write(f"Время выполенения getMin: {time_getMin()}\n")
f.write(f"Время выполнения getMax: {time_getMax()}\n")
f.write(f"Время выполнения getSum: {time_getSum()}\n")
f.write(f"Время выполнения getMult: {time_getMult()}\n")
f.close()
