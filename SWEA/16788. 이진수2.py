T = int(input())
for tc in range(1, T + 1):
  n = float(input())
  
  cnt = 0
  binary = ''

  while n > 0:
    temp = n * 2
    binary += str(temp)[0]  # 정수 부분 저장
    n = temp - int(temp)  # 소수 부분 저장
    cnt += 1

    if cnt > 13:  # 13자리 이상일 경우 중단
      break
    
  if cnt > 12:
    print(f'#{tc} overflow')
  else:  # cnt <= 12
    print(f'#{tc} {binary}')