N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_v = arr[i] + arr[j] + arr[k]
            if M - ans > M - sum_v and M - sum_v >= 0:
                ans = sum_v

print(ans)
