import sys
sys.stdin = open("input.txt", "r")

arr = [list(map(int, input().split())) for _ in range(N)]
lst = []  # 사회자가 부르는 숫자 1차원 배열 생성

for _ in range(5):
  lst += list(map(int, input().split()))

position_lst = [0] * 26 # 번호에 해당하는 좌표의 위치를 저장. 1부터 25까지이므로 26까지 생성

for i in range(5):
  for j in range(5):
    position_lst[arr[i][j]] = (i, j)

# v[0] : 열 누적을 체크할 배열
# v[1] : 행 누적을 체크할 배열
# v[2] : 우하향 대각선 누적 체크 배열
# v[3] : 우상향 대각선 누적 체크 배열
v = [[0] * 9 for _ in range(4)]  

for num in lst:  # 사회자가 부르는 숫자
  i, j = position_lst[num]  # 숫자에 해당하는 좌표를 불러온다.
  v[0][j] += 1  # 해당 열에 누적하여 표시
  v[1][i] += 1  # 해당 행에 누적하여 표시
  v[2][i-j] += 1  # 우하향 대각선에 누적하여 표시
  v[3][i+j] += 1  # 우상향 대각선에 누적하여 표시

  cnt = 0

  for temp_lst in v:
    cnt += temp_lst.count(5)  # 빙고 한 줄이 완성된 개수를 누적

  if cnt >= 3:  # 빙고가 3줄 이상인 경우
    break

print(sum(v[0]))  # 누적된 개수는 v 배열 모두 동일하므로 아무 v나 합하여 출력


