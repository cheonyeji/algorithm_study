# 2023-04-12
# 프로그래머스 고득점 kit - DFS/BFS
# https://school.programmers.co.kr/learn/courses/30/lessons/43162
# 소요 시간 : 16:47 ~ 16:58 (10m)

from collections import deque


def bfs(graph, visited, start):
    visited[start] = True
    queue = deque([start])

    while queue:
        i = queue.popleft()
        for v in range(len(graph[i])):
            if i != v and graph[i][v] == 1 and not visited[v]:
                queue.append(v)
                visited[v] = True


def solution(n, computers):
    answer = 0
    visited = [False] * (n)

    for i in range(n):
        if not visited[i]:
            bfs(computers, visited, i)
            answer += 1
    return answer
