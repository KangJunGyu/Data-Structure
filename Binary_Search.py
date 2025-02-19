def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1 # 값을 못 찾은 경우

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1 # 값 못 찾음
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


arr = [1, 3, 5, 7, 9, 11, 13]
target = 11
print(binary_search_iterative(arr, target))
print(binary_search_recursive(arr, target, 0, len(arr) - 1))