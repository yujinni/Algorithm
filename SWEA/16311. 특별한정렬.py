T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    for i in range(N):
        for j in range(i + 1, N):
            if i % 2 == 0:
                if num_list[j] > num_list[i]:
                    num_list[j], num_list[i] = num_list[i], num_list[j]
            else:
                if num_list[j] < num_list[i]:
                    num_list[j], num_list[i] = num_list[i], num_list[j]
    print(f'#{tc}', *num_list[:10])
    