def partition(arr, start, end):
    pivot = start  # 첫 번째 인덱스를 pivot으로 지정
    left = start + 1
    right = end

    while left <= right:
        while left <= right and arr[left] <= arr[pivot]:
            left += 1
        while left <= right and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:  # 엇갈린 경우
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:  # left < right
            arr[left], arr[right] = arr[right], arr[left]

    return right  # left를 반환할 경우 quick_sort 함수 안에서 두 번째 quick_sort할 때 쓰이지 않으므로 right 반환


def quick_sort(arr, start, end):
    if start < end:
        s = partition(arr, start, end)

        # 분할 이후 왼쪽과 오른쪽 부분에서 각각 퀵 정렬 수행
        quick_sort(arr, start, s - 1)
        quick_sort(arr, s + 1, end)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, N - 1)
    print(f'#{tc} {arr[N/2]}')
    

