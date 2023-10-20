N, M = map(int, input().split())

arr_a = [list(map(int, input().split())) for _ in range(N)]
arr_b = [list(map(int, input().split())) for _ in range(N)]

ans = []

for i in range(N):
    row = []
    for j in range(M):
        row.append(arr_a[i][j] + arr_b[i][j])
    ans.append(row)

for row in ans:
    print(*row)

