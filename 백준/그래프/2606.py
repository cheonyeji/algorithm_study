# 2023-09-03 (소요시간 : 10m)
# 그래프 [실버3. 백준 2606 바이러스] (https://www.acmicpc.net/problem/2606)

from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
edge = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(edge):
    n1, n2 = map(int, input().split(" "))
    # 양방향 연결
    graph[n1].append(n2)
    graph[n2].append(n1)

visit = [False for _ in range(N + 1)]


def bfs(start):
    q = deque([start])
    visit[start] = True
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if not visit[next_node]:
                visit[next_node] = True
                q.append(next_node)


bfs(1)

answer = 0
for i in range(2, N + 1):
    if visit[i]:
        answer += 1

print(answer)
