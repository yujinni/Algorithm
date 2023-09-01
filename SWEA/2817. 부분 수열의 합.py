T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split()) 
    arr = list(map(int, input().split()))

    cnt = 0  # 부분집합의 합이 K가 되는 경우의 수

    for i in range(1 << N):  
        s = 0  # 부분집합의 합

        for j in range(N):
            if i & (1 << j):
                s += arr[j]
                
        if s == K:  # 부분집합의 합이 구하고자 하는 합과 일치하는 경우
            cnt += 1

    print(f'#{tc} {cnt}')