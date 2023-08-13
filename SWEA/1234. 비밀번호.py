T = 10

for tc in range(1, T+1):
    N, M = input().split()
    N = int(N)
    
    stack = []

    for r in M:
        if r not in stack:
            stack.append(r)
        else:
            if r == stack[-1]:
                stack.pop()
            # else:
            #     stack.append(r)

    ans = ''.join(stack)

    print(f'#{tc} {ans}')
