from heapq import heappush, heappop

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
T = int(input())
INF = int(1e9)


def dijkstra():
    q = []
    fuel[0][0] = 0
    heappush(q, (0, 0, 0))  # 가중치 0, 시작 위치 좌표 (0, 0)

    while q:
        w, r, c = heappop(q)  # w: 가중치, r: 행 번호, c: 열 번호

        # 방금 꺼내온 r, c까지의 사용량 w가 이전에 계산해놓은 r,c까지의 사용량보다 크면 계산 X
        if fuel[r][c] < w:
            continue

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                height_diff = 0
                if arr[nr][nc] > arr[r][c]:  # nr, nc가 r, c보다 높은 위치인 경우
                    height_diff = arr[nr][nc] - arr[r][c]

                # nr, nc까지 이동하는데 사용한 연료량 = r, c까지 이동하는데 사용한 연료량 + 기본 사용량(1) + 높이 차
                # 이전에 계산해놓은 nr, nc까지 이동하는데 사용한 연료량보다 작으면 갱신
                cost = fuel[r][c] + height_diff + 1
                if cost < fuel[nr][nc]:  # 새로 계산한 연료량이 이전보다 작을 경우 갱신
                    fuel[nr][nc] = cost
                    # 갱신이 일어날 때만 추가
                    heappush(q, (cost, nr, nc))


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    fuel = [[INF] * N for _ in range(N)]

    dijkstra()

    print(f'#{tc} {fuel[N-1][N-1]}')