# 2023-06-26
# 백준 - 백트래킹
# https://www.acmicpc.net/problem/1405
# 소요 시간 : 17:50 ~ 18:35 (45m)

"""
상하좌우 모두 이동 가능하도록 방문그래프visited는 최대이동수x2로 설정
성공한 경우의 확률을 모두 더해주면 되는 문제
만약 N번 이동했다면 지금까지의 확률을 더해주고 return
return된 경우, 방문처리된 것 false로, 확률 다시 원래대로, 이동횟수 -1 해서 반복문 다시 돌기
"""

from sys import stdin

input = stdin.readline
N, *percentage = map(int, input().split())

visited = [[False for _ in range(30)] for _ in range(30)]

visited[15][15] = True  # start좌표 (15, 15)


cnt = 0
p = 1
answer = 0


def move(i):
    if i == 0:
        return [0, 1]
    elif i == 1:
        return [0, -1]
    elif i == 2:
        return [1, 0]
    elif i == 3:
        return [-1, 0]


def dfs(x, y):
    global cnt, p, answer
    if cnt == N:
        answer += p
        return

    for i in range(4):
        if percentage[i] == 0:
            continue
        nx = x + move(i)[0]
        ny = y + move(i)[1]

        if visited[nx][ny]:
            continue

        visited[nx][ny] = True
        cnt += 1
        p *= percentage[i] / 100

        dfs(nx, ny)
        cnt -= 1
        p /= percentage[i] / 100
        visited[nx][ny] = False


dfs(15, 15)
print(answer)
