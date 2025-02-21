def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1] or (left[i][1] == right[j][1] and left[i][0] < right[j][0]):
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


N = int(input())
meeting = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
finish_time = 0
sorted_meeting = mergeSort(meeting)

for start, end in sorted_meeting:
    if start >= finish_time:
        # print(start, end, finish_time)
        cnt += 1
        finish_time = end

print(cnt)