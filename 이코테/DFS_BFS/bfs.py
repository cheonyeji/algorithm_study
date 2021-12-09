from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

visited = [False] * 9

bfs(graph, 1, visited)

# 인접행렬로 짜기
graph2 = [
    [1, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 1],
]


def bfsM(graph, start):
    visited = [False] * len(graph)
    answer = []

    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        answer.append(v)
        for i in range(len(graph[v])):
            if graph[v][i] == 1 and not visited[i] and v != i:
                queue.append(i)
                visited[i] = True
    return answer


print(bfsM(graph2, 0))
