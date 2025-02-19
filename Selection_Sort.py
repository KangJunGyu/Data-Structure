def selectionSort(arr):
    for i in range(len(arr) - 1): # 마지막 요소는 알아서 정렬되니까
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [66, 33, 22, 11, 44, 77, 55]
selectionSort(arr)
print(arr)