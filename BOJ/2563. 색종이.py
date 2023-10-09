N = int(input())
paper = [[0] * 100 for _ in range(100)]
cnt = 0

for _ in range(N):
    x, y = map(int, input().split())

    for r in range(y, y + 10):
        for c in range(x, x + 10):
            paper[r][c] = 1


for i in paper:
    cnt += i.count(1)

print(cnt)
