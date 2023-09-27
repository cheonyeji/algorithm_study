# 2023-09-27 (소요시간 : 30m + 해설참고)
# 문제집 https://www.acmicpc.net/workbook/view/8708
# 실버2. https://www.acmicpc.net/problem/2512


"""
이분탐색인것까지는 잘 캐치
최종적으로 리턴해줘야하는 값이 end란 것에 주의
"""

from sys import stdin

input = stdin.readline

N = int(input())
data = list(map(int, input().split(" ")))
M = int(input())

answer = 0


def search(M, start, end):
    while start <= end:
        mid = (start + end) // 2

        total = 0
        for num in data:
            if num > mid:
                total += mid
            else:
                total += num

        if total == M:
            return mid

        # 상한액을 올려도 됨
        if total <= M:
            start = mid + 1
        else:
            end = mid - 1

    return end


def solution(M):
    result = search(M, 1, max(data))
    print(result)


solution(M)
