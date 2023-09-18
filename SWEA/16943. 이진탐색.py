T = int(input())

L = 0  # 왼쪽 방향
R = 1  # 오른쪽 방향

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()  # 이진탐색 진행을 위한 오름차순 정렬

    cnt = 0

    for target in B:
        start = 0
        end = N - 1
        dir = -1  # 어느 방향을 탐색했는지. 초기값은 방향 무관

        while start <= end:
            mid = (start + end) // 2

            if target == A[mid]:
                cnt += 1
                break

            elif target < A[mid]:  # target이 중간값보다 작아 왼쪽 탐색을 이어나가야 하는 경우
                if dir == L:  # 이미 왼쪽 구간을 탐색한 경우 - 왼쪽만 탐색하게 되어 조건 충족 X
                    break
                else:  # 이전 탐색 위치가 오른쪽인 경우
                    end = mid - 1
                    dir == L  # 왼쪽 탐색함으로써 양 방향 탐색이라는 조건 충족 O

            else:  # target > A[mid]
                if dir == R:
                    break
                else:
                    start = mid + 1
                    dir == R

    print(f'#{tc} {cnt}')