def baby_gin(cnts, idx):
    if cnts[idx] == 3:
        return 1
    for i in (idx-2, idx-1, idx):
        if 0 <= i <= 7 and cnts[i] > 0 and cnts[i+1] > 0 and cnts[i+2] > 0:
            return 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))

    cnts1 = [0]*10
    cnts2 = [0]*10

    ans = 0

    for i in range(len(arr)):
        if i % 2 == 0:
            cnts1[arr[i]] += 1
            if baby_gin(cnts1, arr[i]):
                ans = 1
                break
        else:
            cnts2[arr[i]] += 1
            if baby_gin(cnts2, arr[i]):
                ans = 2
                break

    print(f'#{tc} {ans}')