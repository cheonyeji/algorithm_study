# 2022-01-17
# 이코테 ch15 이진 탐색 문제 Q27. 정렬된 배열에서의 특정 수의 개수 구하기

from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

n, x = map(int, input().split())
data = list(map(int, input().split()))  # 정렬된 상태로 입력받음 -> 따로 정렬해줄 필요X

# right_index = bisect_right(data, x)
# left_index = bisect_left(data, x)

# result = right_index - left_index

# if result == 0:
#     print(-1)
# else:
#     print(result)

"""
TC 1 -> 결과 : 4
7 2
1 1 2 2 2 2 3
TC 2 -> -1
7 4
1 1 2 2 2 3
"""

###############
# ver2. 직접 이진탐색 구현


def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    # 중간점의 값보다 target이 작거나 같은 경우 왼쪽 확인 (여기에서는 같은 경우도 들어가야 함)
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    # 중간점의 값 < target인 경우 오른쪽 확인
    else:
        return first(array, target, mid + 1, end)


def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    # 중간점의 값보다 target이 작은 경우 왼쪽 확인 (같은 경우 들어가서는 X)
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    # 중간점의 값 < target인 경우 오른쪽 확인
    else:
        return last(array, target, mid + 1, end)


def count_by_value(array, x):
    n = len(array)
    first_index = first(array, x, 0, n - 1)

    # x가 존재하지 않는 경우
    if first_index == None:
        return 0  # 값이 0개

    last_index = last(array, x, 0, n - 1)

    return last_index - first_index + 1  # +1 해줘야 개수


count = count_by_value(data, x)

if count == 0:
    print(-1)
else:
    print(count)
