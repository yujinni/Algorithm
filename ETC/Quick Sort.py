array = [11, 45, 23, 81, 28, 34]


def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start  # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 값을 찾을 때까지 반복
        while left > start and array[left] < array[pivot]:
            left += 1
        # 피벗보다 작은 값을 찾을 때까지 반복
        while right <= end and array[right] > array[pivot]:
            right -= 1
        if left > right:  # 엇갈린 경우
            array[right], array[pivot] = array[pivot], array[right]  # 작은 값과 피벗을 교체
        else:  # 엇갈리지 않은 경우
            array[left], array[right] = array[right], array[left]  # 작은 값과 큰 값을 교체

    # 분할 이후 왼쪽과 오른쪽 부분에서 각각 퀵 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


quick_sort(array, 0, len(array)-1)
print(array)