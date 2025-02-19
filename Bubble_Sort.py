def bubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i): #맨 뒤 요소는 이미 최댓값이므로 정렬 연산에 포함 x
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [66, 33, 22, 11, 44, 77, 55]
bubbleSort(arr)
print(arr)