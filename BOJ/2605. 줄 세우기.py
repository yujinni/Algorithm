N = int(input())  # 학생 수
arr = list(map(int, input().split()))
ans = []  # 최종적으로 줄을 선 학생들의 번호가 담긴 배열

for i in range(N):
    ans.insert(i - arr[i], i + 1)

for num in ans:
    print(num, end=' ')