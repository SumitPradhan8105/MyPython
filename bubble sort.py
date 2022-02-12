
def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("Sorted Array is: ")
    for i in range(len(arr)):
        print(f"{arr[i]}")
arr = [34, 45, 56, 12, 22, 23, 67, 89, 57, 99]
bubbleSort(arr)
