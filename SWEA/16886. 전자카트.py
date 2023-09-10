def dfs(n, sm, cur):
    global ans
    if ans <= sm:
        return

    if n == N:
        ans = min(ans, sm + arr[cur][1])  # 현재까지의 소모량 + 1번으로 복귀 비용
        return

    for j in range(2, N + 1):
        if v[j] == 0:
            v[j] = 1
            dfs(n + 1, sm + arr[cur][j], j)
            v[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    ans = 100 * N
    v = [0] * (N + 1)

    dfs(1, 0, 1)
    print(f'#{tc} {ans}')