# Homework 1 - Algorithms

# Level 1
# Task 1
def bingo(n: int):

    for i in range(1, 101):

        if i % 3 == 0 and i % 7 == 0:
            print('BinGo')

        elif i % 3 == 0:
            print('Bin')

        elif i% 7 == 0:
            print('Go')

bingo(100)

# Task 2
def sum_numbers(n: int):
    final_sum = 0
    for i in range(n + 1):
        final_sum = final_sum + i
    print(f'The sum of {n} is {final_sum}')

sum_numbers(7)

# Level 2
# Problem 1
def find_max(a: int, b: int, c: int):
    list = (a,b,c)
    max = list[0]
    for number in list:
        if (number > max):
            max = number
    print('Max:', max)


find_max(10,4,28)


# Problem 2
def leap_year(year: int):
    if year % 100 == 0 and year % 400 != 0:
        print('False')
    elif year % 4 == 0:
        print('True')

leap_year(2000)

# Level 3
def generate_fibonacci_sequence(n: int):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_number = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_number)

    return fib_sequence
print(generate_fibonacci_sequence(10))



