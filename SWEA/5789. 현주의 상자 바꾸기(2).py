T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    arr = [0] * N

    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        arr[L - 1:R] = [i] * (R - L + 1)

    print(f'#{tc}', *arr)
