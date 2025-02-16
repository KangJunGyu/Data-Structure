N = int(input())
exp = input()
val = [int(input()) for _ in range(N)]
alpha = [chr(i) for i in range(65, 65 + N)]
s = []
for i in exp:
    if i in '+-*/':
        b = s.pop()
        a = s.pop()
        if i == '+':
            s.append(a + b)
        elif i == '-':
            s.append(a - b)
        elif i == '*':
            s.append(a * b)
        else:
            s.append(a / b)
    else:
        idx = alpha.index(i)
        s.append(val[idx])
rslt = s.pop()
print(f"{rslt:.2f}")