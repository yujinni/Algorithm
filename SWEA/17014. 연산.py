from collections import deque


def bfs(n):
    q = deque()
    v = [0] * (1000000 + 1)
    v[n] = 1
    q.append(n)

    cnt = 0   # 연산 횟수

    while q:
        size = len(q)

        for _ in range(size):
            a = q.popleft()
            if a == M:
                return cnt
            for i in (a+1, a-1, a*2, a-10):
                if 1 <= i <= 1000000 and v[i] == 0:
                    q.append(i)
                    v[i] = 1

        cnt += 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    print(f'#{tc} {bfs(N)}')