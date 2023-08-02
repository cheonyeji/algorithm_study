def solution(numbers, target):
    answer = 0

    total = 0

    def dfs(node_num, i):
        nonlocal answer, total

        total += node_num

        if i == len(numbers) - 1:
            if total == target:
                answer += 1
            total -= node_num

            return

        dfs(numbers[i + 1], i + 1)
        dfs(-numbers[i + 1], i + 1)

    dfs(numbers[0], 0)
    dfs(-numbers[0], 0)

    return answer


print(solution([1, 1, 1, 1, 1], 3))  # 5
print(solution([4, 1, 2, 1], 4))  # 	2
