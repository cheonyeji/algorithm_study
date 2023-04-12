# 2023-04-12
# 프로그래머스 고득점 kit - DFS/BFS
# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 소요 시간 : 12:51 ~ 15:24 (80m) + 해설참고 (1시간 넘어가서 해설을 참고...)


"""
방문 노드를 체크해줄 필요가 없는 문제였다. 어차피 1칸씩 이동하면서 맨 끝까지 본 경우 return해주므로
통상적인 dfs/bfs 문제처럼 visited 배열을 따로 둘 필요 없이 한칸씩 이동해가면서 +/- 해주면 되는 문제였음!!!!
visited가 왜 필요없지? 에 빠져서 visited 이차원배열을 만드는 삽질을 괜히 했다.
"""


def dfs(total, numbers, v, target):
    global count
    if v == len(numbers) and total == target:
        count += 1
        return
    if v == len(numbers):
        return

    dfs(total + numbers[v], numbers, v + 1, target)
    dfs(total - numbers[v], numbers, v + 1, target)


def solution(numbers, target):
    global count
    count = 0
    dfs(0, numbers, 0, target)
    return count


print(solution([1, 1, 1, 1, 1], 3))
