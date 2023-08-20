T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    q = []

    for i in range(N):
        head_num = num_list.pop(0)
        q.append(head_num)

    for j in range(M-N):
        num2 = q.pop(0)
        q.append(num2)

    print(f'#{tc} {q[0]}')