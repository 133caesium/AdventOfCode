import hashlib
import time

test1 = 'abcdef'
solution1 = '609043'
test2 = 'pqrstuv'
solution2 = '1048970'
input = 'bgvyzdsv'

def solvePartOne(secretKey):
    testNumber = 0
    result = hashlib.md5(f'{secretKey}{testNumber}'.encode())
    while result.hexdigest()[0:5] != '00000':
        testNumber += 1
        result = hashlib.md5(f'{secretKey}{testNumber}'.encode())
    print(result.hexdigest())
    print(f'The first number giving 5 leading zeros for secretKey "{secretKey}" is {testNumber}')

def solvePartTwo(secretKey):
    testNumber = 0
    result = hashlib.md5(f'{secretKey}{testNumber}'.encode())
    while result.hexdigest()[0:6] != '000000':
        testNumber += 1
        result = hashlib.md5(f'{secretKey}{testNumber}'.encode())
    print(result.hexdigest())
    print(f'The first number giving 6 leading zeros for secretKey "{secretKey}" is {testNumber}')

if __name__ == '__main__':
    start = time.perf_counter_ns()
    solvePartTwo(test1)
    end = time.perf_counter_ns()
    print(f'The time to solve was {(end - start)/1_000_000} ms')

    start = time.perf_counter_ns()
    solvePartTwo(test2)
    end = time.perf_counter_ns()
    print(f'The time to solve was {(end - start)/1_000_000} ms')

    start = time.perf_counter_ns()
    solvePartTwo(input)
    end = time.perf_counter_ns()
    print(f'The time to solve was {(end - start)/1_000_000} ms')