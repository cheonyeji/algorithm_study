# 2022-10-18
# week3 - 재귀함수와 정렬. 하노이 탑 이동 순서
# https://www.acmicpc.net/problem/11729
# 소요시간 : 14:05 ~ 14:10 (5m)

import sys

input = sys.stdin.readline

N = int(input())

# N개의 원판을 해결하기 위해서 N-1개의 원판문제를 해결하자.
def hanoi(start, mid, end, disc):
    if disc == 1:
        print(start, end)
    else:
        # 기둥 1 -> 기둥 2(보조 기둥)으로 N-1개 기둥 이동
        hanoi(start, end, mid, disc - 1)
        # 기둥 1개의 남은 원판 1개 -> 기둥 3으로 이동
        hanoi(start, mid, end, 1)
        # 기둥 2 -> 기둥 3으로 남은 N-1개 이동
        hanoi(mid, start, end, disc - 1)


print(2 ** N - 1)
hanoi(1, 2, 3, N)
