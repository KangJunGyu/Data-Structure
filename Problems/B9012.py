cnt = int(input())
output = []
while cnt != 0:
    s = []
    flg = 0
    par_input = input()
    for idx in range(len(par_input), 0, -1):
        tmp = par_input[idx - 1]
        if tmp == ')':
            s.append(tmp)
            continue
        elif tmp == '(' and s:
            s.pop()
            continue
        else:
            output.append("NO")
            flg = 1
            break

    cnt = cnt - 1
    if flg == 0:
        if not s:
            output.append("YES")
        else:
            output.append("NO")
    else:
        continue


while output:
    print(output.pop(0))

