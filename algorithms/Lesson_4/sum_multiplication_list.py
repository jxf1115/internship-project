# Warm up challenge - Sum and Multiplication in list
# Given an array of integers, calculate sum and multiplication of elements.


def sum_and_mult(arr: list):
    arr_sum = 0
    arr_mult = 1

    for element in arr:
        arr_sum += element
        arr_mult *= element

    print(arr)
    return [arr_sum, arr_mult]

sum_and_mult_list = [1, 7, 3]
print(sum_and_mult(sum_and_mult_list))