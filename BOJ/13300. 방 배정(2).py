import math

N, K = map(int, input().split())

student_info = [[0] * 2 for _ in range(6)]  # 1학년부터 6학년까지

for i in range(N):
    S, V = map(int, input().split())
    student_info[V-1][S] += 1

ans = 0
for j in range(6):
    for k in range(2):
        ans += math.ceil(student_info[j][k] / K)

print(f'{ans}')