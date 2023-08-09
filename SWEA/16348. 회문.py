T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    ans = ""

    # 가로 줄 검토
    for i in range(N): 
        for j in range(N-M+1):
            word_row = ""
            for k in range(M):
                word_row += arr[i][j+k]
            for m in range(M//2):
                if word_row[m] != word_row[M-m-1]:
                    break
            else: 
                ans = word_row


    # 세로 줄 검토
    for j in range(N):  
        for i in range(N-M+1):
            word_col = ""
            for k in range(M):
                word_col += arr[i+k][j]
            cnt = 0  
            for m in range(M//2):
                if word_col[m] != word_col[M-m-1]:
                    break
                if word_col[m] == word_col[M-m-1]:
                    cnt += 1
                if cnt == N//2 -1:
                    ans = word_col

                    
    print(f'#{tc} {ans}')
