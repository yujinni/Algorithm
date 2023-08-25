T = int(input())
for tc in range(1, T + 1):
    word = [list(map(str, input())) for _ in range(5)]
    arr = [[0] * 15 for _ in range(15)]  # 문자열의 최대 길이만큼 배열 형성

    # 각 행을 순회하면서 해당 행의 열 길이만큼 순회
    for i in range(len(word)):  # for i in range(5) 
        for j in range(len(word[i])):  # 각 행의 단어 길이만큼 순회
            arr[i][j] = word[i][j]  # 해당 word 위치의 값을 arr에 할당

    ans = ''  # 출력할 글자
    for k in range(15):  
        for l in range(15):
            if arr[l][k] != 0:  # 세로로 읽어오기 위해 arr[l][k]로 검사
                ans += arr[l][k]   # ans에 읽어온 단어들 더해주기

    print(f'#{tc} {ans}')