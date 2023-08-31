T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    max_cnt = 0

    for s1 in str1:
        cnt = 0
        for s2 in str2:
            if s1 == s2:
                cnt += 1

        max_cnt = cnt if max_cnt < cnt else max_cnt

    print(f'#{tc} {max_cnt}')