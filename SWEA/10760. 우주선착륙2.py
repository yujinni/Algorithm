T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [1, 1, 0, -1, -1, -1, 0, 1]  # 우, 우상, 상, 좌상, 좌, 좌하, 하, 우하
    dc = [0, 1, 1, 1, 0, -1, -1, -1]
    ans = 0

    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(8):
                nr = i + dr[k]
                nc = j + dc[k]
                if 0 <= nr < N and 0 <= nc < M:
                    if arr[nr][nc] < arr[i][j]:
                        cnt += 1
            if cnt >= 4:
                ans += 1

    print(f'#{tc} {ans}')