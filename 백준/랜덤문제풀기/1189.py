# 2023-10-02
# 백준 컴백홈 https://www.acmicpc.net/problem/1189

# DFS로 풀기 (모든 경우 다 봐야함)
# 방문하지 않은 좌표 & T가 아니면 방문

from sys import stdin

input = stdin.readline

R, C, K = map(int, input().split(" "))
graph = [list(input().rstrip()) for _ in range(R)]

visited = [[False for _ in range(C)] for _ in range(R)]
count = [[0 for _ in range(C)] for _ in range(R)]

answer = 0


def dfs(r, c):
    global R, C, K, answer
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    if r == 0 and c == C - 1 and count[r][c] == K:
        answer += 1
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            if not visited[nr][nc] and graph[nr][nc] != "T":
                visited[nr][nc] = True
                count[nr][nc] = count[r][c] + 1
                dfs(nr, nc)
                visited[nr][nc] = False
                count[nr][nc] = 0


count[R - 1][0] = 1
visited[R - 1][0] = True
dfs(R - 1, 0)

print(answer)
