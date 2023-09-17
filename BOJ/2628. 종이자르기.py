w, h = map(int, input().split())
cut_num = int(input())
width = [0, w]
height = [0, h]

for _ in range(cut_num):
  num1, num2 = map(int, input().split())

  if num1 == 0:  # 가로 자르기
    height.append(num2)
  else:  # 세로 자르기
    width.append(num2)
  
width.sort()  
height.sort()  

ans = 0

for i in range(len(width) - 1):
  for j in range(len(height) - 1):
    x = width[i+1] - width[i]
    y = height[j+1] - height[j]
    ans = max(ans, x*y)

print(ans)