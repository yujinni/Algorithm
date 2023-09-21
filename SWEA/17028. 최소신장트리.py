def find_set(x):
    if x != p[x]:
        x = p[x]

    return x


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if y > x:
        p[y] = x
    else:
        p[x] = y


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edge = []

    for _ in range(E):
        s, e, w = map(int, input().split())  # 시작 노드, 도착 노드, 가중치
        edge.append((w, s, e))

    edge.sort()  # 가중치 기준으로 오름차순 정렬

    p = [i for i in range(V + 1)]  # 노드 번호가 0번부터 시작하므로 range(V + 1)
    cnt = 0  # 고른 간선의 개수
    total = 0  # 가중치의 합

    for w, s, e in edge:
        if find_set(s) != find_set(e):  # 사이클이 형성되지 않은 경우
            cnt += 1
            union(s, e)  # 같은 집합으로 묶어줌으로써 대표 노드를 일치시켜준다.
            total += w
            if cnt == V:  # MST 구성이 끝난 경우
                break

        
    print(f'#{tc} {total}')



