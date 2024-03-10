# 2023-10-03
# 백준 종이 조각 https://www.acmicpc.net/problem/14391
#

# 가로, 세로 중 더 긴 방향으로 최대한 길게 잘라줄것
# 0 인 경우만 패스

from sys import stdin

input = stdin.readline

N, M = map(int, input().split(" "))  # N : row, M : col
data = [list(input().rstrip()) for _ in range(N)]

answer = 0
# 더 큰 수가 나올 수 있는 방향 보기

# ans1 = 0
# c = 0
# while c < M:
#     num = ""
#     for r in range(N):
#         num += data[r][c]
#     ans1 += int(num)
#     c += 1
# ans2 = 0
# r = 0
# while r < N:
#     num = ""
#     for c in range(M):
#         num += data[r][c]
#     ans2 += int(num)
#     r += 1
# answer = max(ans1, ans2)

# print(answer)

isUsed = [[False for _ in range(M)] for _ in range(N)]

for r in range(N):
    for c in range(M):
        if data[r][c] != '0':
            # 더 긴 방향으로 자르기
            if N-r>M-c:

            elif N-r<M-c:

            else:
                # 더 큰 숫자로 자르기


# if N > M:
#     # 세로로 자르는 것을 우선하기
    
                
#     c = 0
#     while c < M:
#         num = ""
#         for r in range(N):
#             num += data[r][c]
#         answer += int(num)
#         c += 1

# elif N < M:
#     # 가로로 자르기
#     r = 0
#     while r < N:
#         num = ""
#         for c in range(M):
#             num += data[r][c]
#         answer += int(num)
#         r += 1

# else:
#     # 더 큰 수가 나올 수 있는 방향 보기
#     ans1 = 0
#     c = 0
#     while c < M:
#         num = ""
#         for r in range(N):
#             num += data[r][c]
#         ans1 += int(num)
#         c += 1

#     ans2 = 0
#     r = 0
#     while r < N:
#         num = ""
#         for c in range(M):
#             num += data[r][c]
#         ans2 += int(num)
#         r += 1
#     answer = max(ans1, ans2)


print(answer)
