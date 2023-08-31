# 2023-08-31 (소요시간 : 못 풀어서 해설 참고)
# 구현, 그리디 [실버3. 백준 1783 병든 나이트] (https://www.acmicpc.net/problem/1783)

from sys import stdin

input = stdin.readline

N, M = map(int, input().split(" "))  # 세로 길이 N (row) 가로길이 M (col)

answer = 0
if N == 1:
    answer = 1
elif N == 2:
    if 1 <= M <= 6:
        answer = (M + 1) // 2
    else:
        answer = 4
elif N >= 3:
    if 1 <= M <= 6:
        answer = min(M, 4)
    else:
        answer = M - 2

print(answer)
