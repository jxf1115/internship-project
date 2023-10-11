# Lesson 4 Algorithms Homework - Julio Fernandez

# Task 1
def sum_even_and_product_odd(arr: list):
    sum_even = 0
    product_odd = 1

    for number in arr:
        if number % 2 == 0:
            sum_even += number
        else:
            product_odd *= number

    return [sum_even, product_odd]

list1 = [1, 2, 3, 4]
print(sum_even_and_product_odd(list1))


# Task 2

def sum_between_range(arr: list, min_val: int, max_val: int):
    result = 0
    for number in arr:
        if number >= min_val and number <= max_val:
            result += number
    return result

arr = [3, 2, 1, 4, 10, 8, 7, 6, 9, 5]
min_val_test = 3
max_val_test = 7

print(sum_between_range(arr, min_val_test, max_val_test))


# Task 3

def buy_and_sell_stock_2(prices: list):
    profit = 0
    # [7, 1, 5, 3, 6, 4]

    for i in range(len(prices) - 1):   # i = 0
        if prices[i + 1] - prices[i] > 0:
            profit += prices[i + 1] - prices[i]

    return profit

test_prices_2 = [7, 1, 5, 3, 6, 4]
print(buy_and_sell_stock_2(test_prices_2))

# Task 4

def plus_one(arr: list):
    arr[-1] += 1

    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        else:
            arr[i] = 0
            arr[i - 1] += 1

    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)

    return arr

list_4 = [1, 2, 9]
print(plus_one(list_4))