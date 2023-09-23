code = {
  '0001101': 0,
  '0011001': 1,
  '0010011': 2,
  '0111101': 3,
  '0100011': 4,
  '0110001': 5,
  '0101111': 6,
  '0111011': 7,
  '0110111': 8,
  '0001011': 9,
}

T = int(input())
for tc in range(1, T + 1):
  N, M = map(int, input().split())
  
  arr = []
  binary = ''

  for n in range(N):
    temp = input()
    arr.append(temp)

    if not binary and '1' in temp:
      binary = temp

  p = M - binary[::-1].index('1')
  binary = binary[(p - 56):p]

  number = []
  for i in range(0, 56, 7):
    number.append(code[binary[i:i + 7]])

  odd = 0
  even = 0
  for i in range(8):
    if i == 7:
      if (odd * 3 + even + number[i]) % 10 == 0:
        print(f'#{tc} {odd + even + number[i]}')
      else:
        print(f'#{tc} {0}')

    elif i % 2:
      even += number[i]

    else:
      odd += number[i]
      