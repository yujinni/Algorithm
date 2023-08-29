T = int(input())

for tc in range(1, T + 1):
    bracket = input()
    stack = []

    for e in bracket:
        if e == '(' or e == '{':
            stack.append(e)

        elif e == ')' or e == '}':
            if not stack:  # 빈 스택인 경우
                stack.append(e)
            else:  # 닫는 괄호가 나온 상태이고 스택은 비어있지 않은 경우
                if (e == ')' and stack[-1] == '(') or (e == '}' and stack[-1] == '{'):
                    stack.pop()
                else: 
                    pass
            
    if not stack:  # 빈 스택인 경우
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')