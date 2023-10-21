arr = [list(map(int, input().split())) for _ in range(9)]
ans = 0
r = 0
c = 0

for i in range(9):
    for j in range(9):
        if ans <= arr[i][j]:
            ans = arr[i][j]
            r = i + 1
            c = j + 1

print(ans)
print(r, c)