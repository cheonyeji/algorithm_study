# 2023-04-12
# 프로그래머스 고득점 kit - 완전탐색
# https://school.programmers.co.kr/learn/courses/30/lessons/86971
# 소요 시간 : 11:00 ~ 12:00 (60m)

from collections import deque


def bfs(start, visited, graph, queue):
    count = 1
    visited[start] = True
    queue.append(start)
    while queue:
        x = queue.popleft()
        count += 1
        for i in range(len(graph[x])):
            y = graph[x][i]
            if not visited[y]:
                visited[y] = True
                queue.append(y)
    return count


def solution(n, wires):
    answer = 101
    queue = deque()

    graph = [[] for _ in range(n + 1)]
    for conn in wires:
        graph[conn[0]].append(conn[1])
        graph[conn[1]].append(conn[0])

    for case in wires:
        visited = [False] * (n + 1)
        graph[case[0]].remove(case[1])
        graph[case[1]].remove(case[0])

        num_of_conn_nodes = []
        for i in range(1, n + 1):
            if visited[i]:
                continue
            else:
                num_of_conn_nodes.append(bfs(i, visited, graph, queue))
        answer = min(answer, abs(num_of_conn_nodes[0] - num_of_conn_nodes[1]))

        graph[case[0]].append(case[1])
        graph[case[1]].append(case[0])

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
