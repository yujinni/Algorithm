from heapq import heappop, heappush


def dijkstra(s):  # s: 시작 정점
    q = []
    heappush(q, (0, s))
    distance[s] = 0

    while q:
        w, v = heappop(q)  # w: 가중치, v: 정점 번호

        if distance[v] < w:  # distance[v]: v번까지의 최소 거리
            continue

        for u, uw in adjl[v]:  # u: v와 연결된 정점 번호, uw: v에서 u까지의 거리
            cost = distance[v] + uw
            if distance[u] > cost:
                distance[u] = cost  # 최단 거리 갱신
                heappush(q, (cost, u))


T = int(input())
INF = int(1e9)
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    adjl = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)

    for _ in range(E):
        s, e, w = map(int, input().split())
        adjl[s].append((e, w))

    dijkstra(0)
    print(f"#{tc} {distance[N]}")