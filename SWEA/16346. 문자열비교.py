T = int(input())
for tc in range(1, T+1):
    pattern = input()
    text = input()
    pi = 0
    ti = 0
    ans = 0

    while pi < len(pattern) and ti < len(text):
        if pattern[pi] == text[ti]:
            pi += 1
            ti += 1
        else:
            ti = ti - pi + 1
            pi = 0
        if pi == len(pattern):
            ans = 1
            break

    print(f'#{tc} {ans}')
