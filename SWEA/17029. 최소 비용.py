def bfs(si, sj, ei, ej):
    q = []
    v = [[INF] * N for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = 0

    while q:
        i, j = q.pop(0)
        di = [1, -1, 0, 0]
        dj = [0, 0, -1, 1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] > v[i][j] + 1 + max(arr[ni][nj] - arr[i][j], 0):
                q.append((ni, nj))
                v[ni][nj] = v[i][j] + 1 + max(arr[ni][nj] - arr[i][j], 0)
    return v[ei][ej]


T = int(input())
INF = int(1e9)
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = bfs(0, 0, N-1, N-1)
    print(f'#{tc} {ans}')