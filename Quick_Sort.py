def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]

    return quickSort(left) + middle + quickSort(right)

arr = [66, 33, 22, 11, 44, 77, 55]
arr = quickSort(arr)
print(arr)