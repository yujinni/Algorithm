icp = {'+': 1, '-': 1, '/': 2, '*': 2, '(': 3}
isp = {'+': 1, '-': 1, '/': 2, '*': 2, '(': 0}
 
T = 10
for tc in range(1, T+1):
    N = int(input())
    infix = list(input()) 
    postfix = ''
    stack = []
 
    for i in range(N):
        if infix[i] not in '+-*/':
            postfix += infix[i]
        else:
            while stack and isp[stack[-1]] > icp[infix[i]]:
                postfix += stack.pop()
            stack.append(infix[i])
 
    while stack:
        postfix += stack.pop()
 
    for c in postfix:
        if c not in '+-*/':
            stack.append(int(c))
        else:
            b = stack.pop()
            a = stack.pop()
            if c == '+':
                stack.append(a+b)
 
    print(f'#{tc} {stack.pop()}')