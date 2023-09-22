def recur(level, acc_height):  # acc_height: 탑의 누적 높이
    global ans

    if acc_height >= B:
        ans = min(ans, acc_height)
        return

    if level == N:
        return

    recur(level + 1, acc_height + arr[level])  # 점원을 탑에 포함시킬 경우
    recur(level + 1, acc_height)  # 점원을 탑에 포함시키지 않을 경우


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = int(1e9)
    recur(0, 0)
    print(f'#{tc} {ans - B}')