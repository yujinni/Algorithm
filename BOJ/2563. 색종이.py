N = int(input())  # 색종이의 수
paper = [[0] * 100 for _ in range(100)]  # 가로, 세로가 각각 100인 도화지

for _ in range(N):
    x, y = list(map(int, input().split()))
    for r in range(x, x+10):
        for c in range(y, y+10):
            paper[r][c] = 1

area = 0  # 색종이가 붙은 영역의 넓이
for i in range(N):
    area += paper[i].count(1)

print(area)
