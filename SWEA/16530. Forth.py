T = int(input())

for tc in range(1, T+1):
    arr = list(input().split())
    stack = []

    for i in arr:
        if i in '+-*/' and len(stack) < 2:
            print(f'#{tc} error')
            break
        elif i in '+-*/' and len(stack) >= 2:
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                stack.append(a + b)
            elif i == '-':
                stack.append(a - b)
            elif i == '*':
                stack.append(a * b)
            elif i == '/':
                stack.append(a // b)
        elif i == '.':
            pass
        else:  # 숫자인 경우
            stack.append(int(i))
      
    else:
      if len(stack) == 1:
          print(f'#{tc} {stack[-1]}')
      else:
          print(f'#{tc} error')
      
            