def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = mergeSort(arr[:mid])
    right_half = mergeSort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr
    '''
    - 남은 요소 전부 추가
        - 한쪽 배열이 먼저 소진이 되니까
          요소가 남은 배열을 전부 소진
    '''

arr = [66, 33, 22, 11, 44, 77, 55]
arr = mergeSort(arr)
print(arr)