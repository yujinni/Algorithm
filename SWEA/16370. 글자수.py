T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    ans = 0

    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
        if ans < cnt:
            ans = cnt
    
    print(f'#{tc} {ans}')