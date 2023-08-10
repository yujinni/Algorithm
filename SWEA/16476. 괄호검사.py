T = int(input())

for tc in range(1, T+1):
    bracket = input()
    stack = []

    for e in bracket:
        if e == "(" or e == "{":
            stack.append(e)
        elif e == ")" or e == "}":
            if not stack:  # 빈 스택인 경우
                stack.append(e)
                break
            else:  # 빈 스택이 아닌 경우
                if (e ==")" and stack[-1] == "(") or (e == "}" and stack[-1] == "{"):  # 알맞게 짝지어진 경우
                    stack.pop()
                else:  # 알맞은 짝이 아닌 경우
                    break  # 이미 스택에 요소가 있으므로 append없이 바로 종료

    if not stack:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')

