T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [1, 0, -1, 0] # 우, 상, 좌, 하
    dc = [0, 1, 0, -1]

    max_v = 0  # 꽃가루 수 최댓값

    for r in range(N):
        for c in range(M):
            sum_v = 0  # 상하좌우 합
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < M:
                    sum_v += arr[nr][nc]
            if max_v < sum_v + arr[r][c]:
                max_v = sum_v + arr[r][c]

    print(f'#{tc} {max_v}')