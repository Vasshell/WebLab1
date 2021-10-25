# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def Task1(number):
    nums = []
    while number > 0:
        nums.append(number % 10)
        number = number // 10
    for i in range(int(len(nums) / 2)):
        if nums[i] != nums[len(nums) - 1 - i]:
            return False
    return True


print('Task One:\n')
print('input = 987789\n', 'output:', Task1(987789))
print('input = 1234\n', 'output:', Task1(1234))
print('____')


def Task2(numbers):
    by2 = []
    by3 = []
    by5 = []
    for i in range(int(len(numbers))):
        if numbers[i] % 2 == 0:
            by2.append(numbers[i])
        if numbers[i] % 3 == 0:
            by3.append(numbers[i])
        if numbers[i] % 5 == 0:
            by5.append(numbers[i])
    results = [by2, by3, by5]
    return results


print('Task Two:\n')
print('input = 1,2,3,4,5,6,7,8,9,10\n', 'output:')
result = Task2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for i in range(int(len(result))):
    print(result[i], ' ')
print('____')


def Task3(number):
    nums = []
    negative = 1
    if number < 0:
        negative = -1
        number *= -1
    while number > 0:
        nums.append(number % 10)
        number = number // 10
    nums.reverse()
    result = 0
    for i in range(len(nums)):
        result += int(nums[i]) * negative * 10 ** i
    return result


print('Task Three:\n')
print('input = -123 \n', 'output:', Task3(-123), '\n')
print('input = 120 \n', 'output:', Task3(120), '\n')
print('input = 0 \n', 'output:', Task3(0), '\n')
print('input = 123 \n', 'output:', Task3(123), '\n')
print('____')

from math import fabs


def Task4(number, power):
    x = number
    for i in range(100):
        if fabs(x - ((power - 1) * x + number / x ** (power - 1)) / power) > 0.001:
            x = ((power - 1) * x + number / x ** (power - 1)) / power
        else:
            break
    return x


print('Task Four:\n')
print('input: 11th root of 781 \n', 'output:', Task4(781, 11), '\n')
print('____')


def Task5(number):
    ifPrime = True
    for i in range(2, number):
        if number % i == 0:
            if number != i:
                ifPrime = False
    return ifPrime


print('Task Five:\n')
print('input: 1', 'output:', Task5(1), '\n')
print('input: 18', 'output:', Task5(18), '\n')
print('input: 11', 'output:', Task5(11), '\n')
print('input: 200', 'output:', Task5(200), '\n')
print('input: 17', 'output:', Task5(17), '\n')
print('____')
