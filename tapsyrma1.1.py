arr = [34, 23, 12, 45, 78, 11, 89]


for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print("Selection Sort нәтижесі:", arr)