# 프로그래머스 고득점 kit dfs_bfs 타겟넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165
answer = 0


def dfs(numbers, target, sum, depth):
    global answer
    if depth == len(numbers):
        if sum == target:
            answer += 1
        return
    dfs(numbers, target, sum + numbers[depth], depth + 1)
    dfs(numbers, target, sum - numbers[depth], depth + 1)


def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer


print(solution([1, 1, 1, 1, 1], 3))
