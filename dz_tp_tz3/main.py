import math

with open('numbers.txt') as file:
    readNumbers = file.read()
    numbers = readNumbers.split()


    def getMax(numbers):
        max = float("-inf")
        for i in numbers:
            if max < int(i):
                max = int(i)
        return max


    def getMin(numbers):
        min = float("inf")
        for i in numbers:
            if min > int(i):
                min = int(i)
        return min


    def getSum(numbers):
        sum = 0
        for i in numbers:
            sum += int(i)
        return sum


    def getMult(numbers):
        mult = 1
        for i in numbers:
            mult *= int(i)
        return mult


    def getPower(numbers, power):
        a = []
        for i in numbers:
            powNumber = math.pow(int(i), power)
            a.append(powNumber)
        return a

max = getMax(numbers)
print(max)

min = getMin(numbers)
print(min)

sum = getSum(numbers)
print(sum)

mult = getMult(numbers)
print(mult)

powerList = getPower(numbers, 3)
print(powerList)
