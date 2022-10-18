# 2022-10-18
# week3 - 재귀함수와 정렬. 하노이 탑
# https://www.acmicpc.net/problem/1914
# 소요시간 : 11:25 ~ 12:40 (도저히 감이 오지 않아 해설 참고하여 이해함)

import sys

input = sys.stdin.readline


# start -> end로 원반 disc개 이동
def hanoi(start, mid, end, disc):
    if disc == 1:  #
        print(start, end)  # 출력
    else:
        hanoi(start, end, mid, disc - 1)  # 기둥1 -> 기둥2 (n-1개를 잠시 이동)
        hanoi(start, mid, end, 1)  # 가장 큰 원반 기둥1 -> 기둥 3
        hanoi(mid, start, end, disc - 1)  # 기둥2 -> 기둥3


N = int(input())

print(2 ** N - 1)
if N <= 20:
    hanoi(1, 2, 3, N)
