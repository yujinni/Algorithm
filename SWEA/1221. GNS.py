T = int(input())
arr = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, T+1):
    n = list(map(str, input().split()))
    number_list = list(map(str, input().split()))
    ans = []

    for i in range(10):
        for j in number_list:
            if arr[i] == j:
                ans.append(j)

    print(n[0])
    print(*ans)