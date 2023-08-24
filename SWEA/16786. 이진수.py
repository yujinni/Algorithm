T = int(input())
for tc in range(1, T + 1):
    n, hex_num = input().split()
    n = int(n)

    # hex_num을 이진수로 바꾼 문자열
    hex_to_bin = ''

    for i in range(n):
        ith_num = int(hex_num[i], 16)

        for j in range(3, -1, -1):
            if ith_num & (1 << j) == 0:
                hex_to_bin += '0'
            else:
                hex_to_bin += '1'

    print(f'#{tc} {hex_to_bin}')