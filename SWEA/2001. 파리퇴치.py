T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_v = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    sum_v += arr[x][y]
            if max_v < sum_v:
                max_v = sum_v

    print(f'#{tc} {max_v}')