T = int(input())
for tc in range(T+1):
    arr = list(input())
    stack = []

    for i in arr:
        if not stack:  # 빈 스택인 경우
            stack.append(i)
        elif i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    print(f'#{tc} {len(stack)}')