T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    min_cnt = N * M

    one_cnt = 0
    for w in range(0, N - 2):
        for j in range(M):
            if arr[w][j] != 'W':
                one_cnt += 1

        two_cnt = 0
        for b in range(w + 1, N - 1):
            for j in range(M):
                if arr[b][j] != 'B':
                    two_cnt += 1

            three_cnt = 0
            for r in range(b + 1, N):
                for j in range(M):
                    if arr[r][j] != 'R':
                        three_cnt += 1

            cnt = one_cnt + two_cnt + three_cnt

            if min_cnt > cnt:
                min_cnt = cnt

    print(f'#{tc} {min_cnt}')