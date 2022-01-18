# 2022-01-17
# 이코테 ch15 이진 탐색 문제 Q28. 고정점 찾기

import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))


def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] < mid:  # 오른쪽만 봐도 OK
        return binary_search(array, mid + 1, end)
    else:  # 왼쪽만 봐도 OK
        return binary_search(array, start, mid - 1)


result = binary_search(data, 0, n - 1)

if result == None:
    print(-1)
else:
    print(result)

"""
TC 1 -> 3
5
-15 -6 1 3 7
TC 2 -> 2
7
-15 -4 2 8 9 13 15
TC 3 -> -1
7
-15 -4 3 8 9 13 15
"""

# 어렵게 생각할 것 없이, array[mid] < mid면 왼쪽에서 값이 나올 수가 없다. 값은 중복X, 오름차순 정렬이므로
# array[mid] > mid면 오른쪽에서 값이 나올 수가 없다.
