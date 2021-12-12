# 프로그래머스 고득점kit 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque

network = 1


def bfs(graph, start, visited):
    global network
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in range(len(graph[v])):
            if graph[v][i] == 1 and not visited[i] and v != i:
                queue.append(i)
                visited[i] = True

    # 그래프가 다 연결이 안된 경우
    if False in visited:
        network += 1
        bfs(graph, visited.index(False), visited)
    # 모든 정점을 다 훑은 경우
    else:
        return network


def solution(n, computers):
    visited = [False] * n
    bfs(computers, 0, visited)
    return network
