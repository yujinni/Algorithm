T = int(input())
arr = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for tc in range(1, T+1):
    N = list(map(str, input().split()))
    num_list = list(map(str, input().split()))
    ans = []

    for i in arr:
        for num in num_list:
            if i == num:
                ans.append(i)

    print(N[0])
    print(*ans)