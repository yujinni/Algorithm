def password(arr):
    while True:
        for i in range(1, 6):
            arr.append(arr.pop(0) - i)
            if arr[-1] <= 0:
                arr[-1] = 0
                return arr


T = 10
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    ans = password(num_list)
    print('#{}'.format(tc), *ans)