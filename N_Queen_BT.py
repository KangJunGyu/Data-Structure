def nqueen(n):
    answer = []
    check = [-1] * n # 한 행에 한 퀸만 들어갈 수 있음 - 초기화
    ### check[i] = j -> i 행에는 퀸을 j 열에 놓았다는 뜻

    # 퀸을 배치할 수 있는가
    def is_safe(row):
        for i in range(row):
            print('check[i] == ', check[i])
            print('check[row] == ', check[row])
            # 같은 열에 이미 퀸이 배치된 경우
            if check[i] == check[row]:
                return False # pruning
            # 대각선에 배치된 경우 -> 행의 차 == 열의 차
            if abs(i - row) == abs(check[i] - check[row]):
                return False # pruning
        return True # 탐색 지속

    def dfs(row):
        # dfs 로 마지막 행까지 진행된 경우 + 각 행에 퀸을 모두 놓은 경우 -> base case
        if row >= n:
            result = [["."] * n for _ in range(n)] # 나머지 칸은 . 으로 채우기
            for i in range(n):
                result[i][check[i]] = 'Q' # 퀸이 들어간 자리 result[행][열]
            
            answer.append(result)
            # 2차원 배열을 1차원 문자열 배열로 만들고 싶으면 아래 식을 사용
            ### answer.append(["".join(result[idx]) for idx in range(n)])

            return
        # 그렇지 않은 경우
        for col in range(n):
            check[row] = col
            print('check[', row, '] = ', col)
            if is_safe(row): # pruning 되지 않은 경우 - dfs 탐색 지속
                dfs(row + 1)
            else: print('Pruning')


    dfs(0) # 첫 행부터 시작 - 프로그램 시작

    return answer

ans = nqueen(4)
for _ in range(len(ans)):
    print(ans[_])


