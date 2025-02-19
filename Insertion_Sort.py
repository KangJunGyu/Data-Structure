def insertionSort(arr):
    for i in range(1, len(arr)): # 두번째 요소부터
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        '''
        - 이미 key 자리를 비우고 while을 통과한 값들은 오른쪽으로 한 칸씩 옮겨짐
        - 마지막에 1을 한번 더 뺐으니 1을 다시 더해주는 것.
        '''

arr = [66, 33, 22, 11, 44, 77, 55]
insertionSort(arr)
print(arr)