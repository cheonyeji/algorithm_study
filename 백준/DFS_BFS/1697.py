# 2023-04-19
# 백준 - DFS/BFS
# https://www.acmicpc.net/problem/1697
# 소요 시간 : 17:00~17:20 (20m 고민해보다 도서히 감안와서 해설참고)

"""
이 문제가 최소 시간을 계산해야한다는 점에서 BFS를 고려해야함
그리고 -1, +1, x2만큼 움직이는게 전파된다고 생각하면 될 것
"""

from sys import stdin
from collections import deque

MAX_SIZE = 100001
input = stdin.readline
N, K = map(int, input().split())  # N : 수빈 위치, K : 동생 위치

graph = [-1] * MAX_SIZE
q = deque()
q.append(N)
graph[N] = 0

while q:
    v = q.popleft()
    if v == K:
        break
    movePos = [-1, +1, 2]
    for i in range(3):
        if i == 2:
            nextV = v * 2
        else:
            nextV = v + movePos[i]
        if 0 <= nextV < MAX_SIZE:
            if graph[nextV] == -1 or graph[nextV] > graph[v] + 1:
                graph[nextV] = graph[v] + 1
                q.append(nextV)

print(graph[K])
