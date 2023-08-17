T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    max_num = num_list[0]
    min_num = num_list[0]

    for i in range(1, N):
        if max_num < num_list[i]:
            max_num = num_list[i]
        elif min_num > num_list[i]:
            min_num = num_list[i]

    print(f'#{tc} {max_num - min_num}')

