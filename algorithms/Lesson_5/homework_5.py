# Lesson 5 Algorithms Homework - Julio Fernandez

# Task 1 - Selection Sort
def selection_sort(arr: list):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

test_array = [3, 28, 19, 1, 2, 5, 9, 45, 29]
print(test_array)
print(selection_sort(test_array))


# Task 2 - Bubble Sort
def bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

test_array_2 = [2, 28, 5, 1, 19, 9, 3, 29]
print(test_array_2)
print(bubble_sort(test_array_2))

# Task 3 - Insertion Sort

def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

test_array_3 = [2, 28, 5, 1, 19, 9, 33, 29, 3]
print(test_array_3)
print(insertion_sort(test_array_3))