# 가위 1, 바위 2, 보 3
# 가위(1) < 바위(2)
# 가위(1) > 보(3)
# 바위(2) < 보(3)

# 그룹화
def group(i, j):
    # 종료 조건
    if i == j:
        return i
    
    # 재귀 호출?
    else:
        left = group(i, (i+j)//2)
        right = group((i+j)//2 + 1, j)
        return rsp(left, right)


# 가위바위보 게임
def rsp(left, right):
    if card_list[left] == card_list[right]:
        return left
    elif card_list[left] - card_list[right]



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card_list = list(map(int, input().split()))
    i = 0
    j = N-1
    print(f'#{tc} {group(i, j) + 1}')