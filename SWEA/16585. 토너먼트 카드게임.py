# 그룹화
def tournament(i, j):
    # 종료 조건
    if i == j:
        return i
 
    # 재귀 호출
    else:
        left = tournament(i, (i+j)//2)
        right = tournament((i+j)//2 + 1, j)
 
        return rsp(left, right)
 
 
# 가위바위보 게임
def rsp(left, right):
    if card_list[left] == card_list[right]:
        return left
 
    elif abs(card_list[right] - card_list[left]) == 1:
        if card_list[right] > card_list[left]:
            return right
        else:
            return left
 
    elif abs(card_list[right] - card_list[left]) == 2:
        if card_list[right] < card_list[left]:
            return right
        else:
            return left
 
 
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card_list = list(map(int, input().split()))
    i = 0
    j = N-1
    print(f'#{tc} {tournament(i, j)+1}')