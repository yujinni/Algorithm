N = int(input())  # 색종이의 개수
grid = [[0] * 1001 for _ in range(1001)]

for i in range(1, N+1):  # i에 1부터 시작되는 N 값을 할당해주기 위해 range 1부터 순회
    a, b, width, height = map(int, input().split())
    for j in range(b, b + height):
        grid[j][a:(a + width)] = [i] * width

for k in range(1, N+1):
    ans = 0  # 각 색종이가 보이는 부분의 면적
    for s in range(1001):  # 격자의 최대 칸 개수 만큼 순회
        ans += grid[s].count(k)
    print(ans)