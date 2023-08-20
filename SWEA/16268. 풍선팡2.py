T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flowers = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]  # 우 상 좌 하
    dj = [1, 0, -1, 0]

    max_flowers = 0

    for i in range(N):
        for j in range(M):
            cnt = flowers[i][j]
            for k in range(4):
                for s in range(1, flowers[i][j]+1):
                    ni = i + di[k]*s
                    nj = j + dj[k]*s
                    if 0 <= ni < N and 0 <= nj < M:
                        cnt += flowers[ni][nj]

            if max_flowers < cnt:
                max_flowers = cnt

    print(f'#{tc} {max_flowers}')

