# 2023-09-06 (소요시간 : 1h 풀고 시간초과 못잡아서 해설참고 )
# 그래프, DP [골드3. 백준 1520 내리막길] (https://www.acmicpc.net/problem/1520)
import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

# M : row, N : col
M, N = map(int, input().split(" "))

graph = [list(map(int, input().split(" "))) for _ in range(M)]

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

dp = [[-1 for _ in range(N)] for _ in range(M)]


# dfs(r, c) -> (r, c)에서 출발하여 (N-1, M-1)까지 가는 경우의 수
def dfs(r, c):
    # 재귀함수 종료조건
    if r == M - 1 and c == N - 1:
        return 1

    # 이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴받아
    # 그 경우는 다시 탐색하지 않음
    if dp[r][c] != -1:
        return dp[r][c]

    dp[r][c] = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < M and 0 <= nc < N:
            if graph[nr][nc] < graph[r][c]:
                dp[r][c] += dfs(nr, nc)

    return dp[r][c]


print(dfs(0, 0))
