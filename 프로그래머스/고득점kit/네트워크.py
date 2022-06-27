# 2022-06-27
# 프로그래머스 고득점 kit - dfs/bfs 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162
# 소요 시간 : 13:49 ~ 14:07 (20m)


from collections import deque

answer = 0


def bfs(matrix, visited, v):
    global answer
    q = deque()

    if not visited[v]:
        answer += 1
        visited[v] = True
        q.append(v)

    while q:
        now = q.popleft()
        for i in range(len(matrix[now])):
            # 방문x & 연결된 정점의 경우
            if not visited[i] and matrix[now][i] == 1 and now != i:
                q.append(i)
                visited[i] = True


# 인접행렬 형태로 입력 주어짐
def solution(n, computers):
    visited = [False] * n

    for i in range(n):
        bfs(computers, visited, i)

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
