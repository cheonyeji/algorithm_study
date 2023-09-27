# 2023-09-22 (소요시간 : 90m하다 못풀어서 해설참고)
# https://school.programmers.co.kr/learn/courses/30/lessons/92343


def solution(info, edges):
    visited = [0] * len(info)
    answer = []

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = 1
                if info[c] == 0:
                    dfs(sheep + 1, wolf)
                else:
                    dfs(sheep, wolf + 1)
                visited[c] = 0

    # 루트 노드부터 시작
    visited[0] = 1
    dfs(1, 0)

    return max(answer)


solution(
    [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [
        [0, 1],
        [1, 2],
        [1, 4],
        [0, 8],
        [8, 7],
        [9, 10],
        [9, 11],
        [4, 3],
        [6, 5],
        [4, 6],
        [8, 9],
    ],
)  # 5
