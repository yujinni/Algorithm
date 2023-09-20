def find_parent(x):
    if x == parent[x]:
        return x
    else:
        return find_parent(parent[x])


def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x == y:
        return
    
    if y > x:
        parent[y] = x
    else:
        parent[x] = y


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    parent = [i for i in range(N + 1)]

    for i in range(0, M * 2, 2):
        union_parent(parent[i], parent[i + 1])

    ans = set()
    for i in parent:
        ans.add(find_parent(i))

    print(f'#{tc} {len(ans) - 1}')