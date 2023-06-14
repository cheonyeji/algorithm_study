"""리스트만 쓰는 버전"""

from sys import stdin

input = stdin.readline

# arr = [1, 2, 3, 3, 3, 3, 4, 4]
arr = [3, 5, 7, 9, 1]


def solution(arr):
    counted = []
    arr_counts = []
    answer = []
    for item in arr:
        if not item in counted:
            counted.append(item)
            arr_counts.append(arr.count(item))

    for item in arr_counts:
        if item != 1:
            answer.append(item)

    if len(answer) == 0:
        return [-1]
    else:
        return answer


print(solution(arr))
