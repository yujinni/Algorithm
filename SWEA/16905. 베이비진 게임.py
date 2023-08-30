def baby_gin(cnts, idx):
    if cnts[idx] == 3:
        return 1
    for i in (idx-2, idx-1, idx):  # run인 경우
        if 0 <= i <= 7 and cnts[i] > 0 and cnts[i+1] > 0 and cnts[i+2] > 0:  # 유효한 숫자 카드(0부터 9까지) 범위 내에 있는지 여부
            return 1
    return 0  # run 또는 triplet이 아닌 경우


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))

    cnts1 = [0]*10
    cnts2 = [0]*10

    ans = 0  # break를 하지 않은 경우 무승부로 0 출력

    for i in range(len(arr)):
        if i % 2 == 0:  # 짝수인 경우
            cnts1[arr[i]] += 1  # 플레이어 1에게 추가
            if baby_gin(cnts1, arr[i]):  # 베이비진인지 확인했을 때 true인 경우
                ans = 1
                break
        else:
            cnts2[arr[i]] += 1
            if baby_gin(cnts2, arr[i]):
                ans = 2
                break

    print(f'#{tc} {ans}')