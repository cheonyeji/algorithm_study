# 2023-08-28 (소요시간 : 1h정도 풀고 30m 해설참고해서 마저 풀음)
# 구현 실버2. 백준 3085 사탕게임 https://www.acmicpc.net/problem/3085

from sys import stdin

input = stdin.readline

N = int(input())

board = [list(input().rstrip()) for _ in range(N)]
answer = 0


def check():
    global answer
    for i in range(N):
        cnt = 1
        for j in range(N - 1):
            if board[i][j] == board[i][j + 1]:
                cnt += 1
                answer = max(answer, cnt)
            else:
                cnt = 1

        cnt = 1
        for j in range(N - 1):
            if board[j][i] == board[j + 1][i]:
                cnt += 1
                answer = max(answer, cnt)
            else:
                cnt = 1


for i in range(N):
    for j in range(N):
        # 세로 방향 교환
        if j + 1 < N:
            if board[i][j] != board[i][j + 1]:
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
                check()
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

        # 가로 방향 교환
        if i + 1 < N:
            if board[i][j] != board[i + 1][j]:
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                check()
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(answer)
