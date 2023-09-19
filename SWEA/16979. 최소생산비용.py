def dfs(product):
    global total, Sum

    if product == N:
        if total > Sum:
            total = Sum
        return

    if total <= Sum:
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            Sum += lst[product][i]
            dfs(product + 1)
            visited[i] = 0
            Sum -= lst[product][i]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    Sum = 0
    total = 9999999

    dfs(0)
    print(f'#{tc} {total}')