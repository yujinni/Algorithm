T = 10
for tc in range(1, T+1):
    N = int(input())
    a = input()
    arr = list(a)
    stack = []

    c = arr.pop(1)
    arr.append(c)
    
    for i in arr:
        if i != '+':
            stack.append(int(i))
        elif i == '+' and len(stack) >= 2:
            b = stack.pop()
            a = stack.pop()
            stack.append(a+b)

    print(f'#{tc} {stack[-1]}')