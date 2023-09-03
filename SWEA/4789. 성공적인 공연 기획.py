T = int(input())
for tc in range(1, T + 1):
    arr = list(map(str, input()))

    clap = 0  # 이전까지 박수 친 사람의 수
    people = 0  # 고용해야 하는 사람의 수

    for i in range(len(arr)):
        if arr[i] != 0:
            if clap >= i:
                clap += int(arr[i])
            else:
                people += i - clap
                clap = i + int(arr[i])

    print(f'#{tc} {people}')