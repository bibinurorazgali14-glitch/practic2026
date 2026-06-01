
arr = [34, 23, 12, 45, 78, 11, 89]
n = len(arr)


for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:

            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Bubble Sort нәтижесі:", arr)