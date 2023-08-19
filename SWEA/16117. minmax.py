T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    max_num = num_list[0]
    min_num = num_list[0]

    for i in range(1, N):
        if max_num < num_list[i]:  # 초기 설정해준 값보다 큰 경우
            max_num = num_list[i]  # 최댓값을 해당 값으로 변경
        elif min_num > num_list[i]: # 초기 설정해준 값보다 작은 경우
            min_num = num_list[i]  # 최솟값을 해당 값으로 변경

    print(f'#{tc} {max_num - min_num}')

