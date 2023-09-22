def dfs(r, c, num):  # r : 행, c : 열
    if len(num) == 7:
        result.add(num)
        return
    
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if nr < 0 or nr >= 4:
            continue
        if nc < 0 or nc >= 4:
            continue

        dfs(nr, nc, num + maps[nr][nc])


T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):
    maps = [input().split() for _ in range(4)]
    result = set()  # 중복 제거를 위해 set 활용
    
    # 모든 점을 시작점으로 순회
    for i in range(4):
        for j in range(4):
            dfs(i, j, maps[i][j])

    print(f'#{tc} {len(result)}')