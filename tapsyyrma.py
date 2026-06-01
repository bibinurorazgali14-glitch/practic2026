# 1. Сызықтық іздеу (Linear Search)
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f"Элемент индексі: {i}"
    return "Табылмады"


# 2. Бинарлық іздеу (Binary Search)
def binary_search(sorted_arr, target):
    low = 0
    high = len(sorted_arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_arr[mid] == target:
            return f"Элемент индексі: {mid}"
        elif sorted_arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return "Табылмады"


# Тексеру
numbers = [10, 23, 35, 47, 59, 70, 88]  # сұрыпталған массив
print(binary_search(numbers, 47))  # Нәтиже: Элемент индексі: 3