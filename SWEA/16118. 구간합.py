T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split()) 
    num_list= list(map(int, input().split()))

    max_sum = 0  
    min_sum = 10000 * M 

    for i in range(N - M + 1):  # 구간합을 진행하는 횟수
        sub_sum = 0
        for j in range(M):
            sub_sum += num_list[i + j]

        max_sum = sub_sum if sub_sum > max_sum else max_sum
        min_sum = sub_sum if sub_sum < min_sum else min_sum

    print(f'#{tc} {max_sum - min_sum}')