T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pizza_list = list(map(int, input().split()))
    next_i = 0  # 다음에 꺼낼 피자 인덱스
    oven = [0] * 1000
    ofront = orear = -1

    for i in range(N):
        orear += 1  # 오븐에 피자 넣기
        oven[orear] = [i, pizza_list[i]]  # [피자 번호, 치즈 양]
        next_i += 1

    remain = N  # 오븐에 남아있는 피자 개수
    last_idx = -1  # 마지막에 꺼낸 피자의 인덱스

    while True:  # 모든 피자의 치즈가 녹을 때까지 반복
        ofront += 1
        pizza_idx, pizza = oven[ofront]  # 피자를 하나 꺼냄
        pizza //= 2  # 치즈를 녹임

        if pizza != 0:  # 남은 치즈 양이 0이 아닐 경우
            orear += 1  # 다시 오븐에 넣기
            oven[orear] = [pizza_idx, pizza]  # [피자 번호, 치즈 양]

        else:  # 남은 치즈 양이 0이 된 경우
            if next_i < M:  # 오븐에 넣을 피자가 남아있는 경우
                orear += 1  # 남아있는 피자 1개 오븐에 넣기
                oven[orear] = [next_i, pizza_list[next_i]]
                next_i += 1  # 하나 꺼냈으므로 다음에 꺼낼 피자 번호 인덱스 1 증가

            else:  # 오븐에 넣을 피자가 남아있지 않은 경우
                remain -= 1  # 오븐에 있는 피자를 뺀다.
                if remain == 0:  # 오븐에 피자를 모두 꺼낸 경우
                    last_idx = pizza_idx  # 현재 꺼낸 피자 인덱스가 마지막으로 꺼낸 게 된다.
                    break  # 반복 종료

    print(f'#{tc} {last_idx + 1}')


