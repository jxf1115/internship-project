# Homework 3 Algorithms - Julio Fernandez

# Task 1

def find_two_lowest(arr: list):
    arr.sort()
    return(arr[0], arr[1])

list1 = [28, 15, 3, 29, 1, 28, 2]

print(find_two_lowest(list1))



# Task 2

def invert_list(arr: list):
    for i in range(len(arr)):
        print(arr)
        arr[i] = -arr[i]
    return arr

list2 = [1, 5, -2, 4]
print(invert_list(list2))

# Task 3
def max_diff(arr: list):

    if len(arr) == 0:
        return 0
    arr.sort()
    print(arr)

    return arr[-1] - arr[0]

list2 = [28, 15, 3, 29, 1, 28, 2]

print(max_diff(list2))


# Task 4

def count_larger_neighbor(arr: list):
    count = 0

    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            count += 1

    return count

list4 = [2, 56, 7, 21, 22, 19, 26]
print(count_larger_neighbor(list4))


# Task 5

def subtract_minimum(arr: list):
    min_element = min(arr)

    for i in range(len(arr)):
        arr[i] = arr[i] - min_element

    return arr

list5 = [9, 2, 5, 4, 7, 6, 1]
print(subtract_minimum(list5))

