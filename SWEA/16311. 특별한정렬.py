T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    for i in range(N):
        for j in range(i + 1, N):
            # 해당 인덱스를 그 뒤의 모든 인덱스와 비교
            if i % 2 == 0:  # 짝수 번째 인덱스에는 큰 값부터 내림차순 정렬되도록
                if num_list[j] > num_list[i]:
                    num_list[j], num_list[i] = num_list[i], num_list[j]
            else:  # 홀수 번째 인덱스에는 작은 값부터 오름차순 정렬되도록
                if num_list[j] < num_list[i]:
                    num_list[j], num_list[i] = num_list[i], num_list[j]
    print(f'#{tc}', *num_list[:10])  # 언패킹하여 10개의 숫자 출력
    