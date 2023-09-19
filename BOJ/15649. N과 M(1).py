def dfs():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return

    for num in range(1, N + 1):
        if num not in arr:
            arr.append(num)
            dfs()
            arr.pop()


N, M = list(map(int, input().split()))
arr = []
dfs()

