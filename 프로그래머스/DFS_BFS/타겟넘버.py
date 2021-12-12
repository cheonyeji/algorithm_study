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
