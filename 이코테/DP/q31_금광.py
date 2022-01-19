# 2022-01-19
# 이코테 ch16 다이나믹 프로그래밍 Q31. 금광

t = int(input())


def solution():
    n, m = map(int, input().split())
    # (1,1)부터 시작하려고 n+1 * m+1 크기의 배열 선언 및 초기화
    g = [[0] * (m + 1) for _ in range(n + 1)]

    data = list(map(int, input().split()))  # 일렬로 쭉 입력받음

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            g[i][j] = data[j - 1 + m * (i - 1)]

    max_gold = 0
    for c in range(2, m + 1):
        for r in range(1, n + 1):
            # 위 존재x
            if r == 1:
                g[r][c] += max(g[r][c - 1], g[r + 1][c - 1])
            # 아래 존재x
            elif r == n:
                g[r][c] += max(g[r][c - 1], g[r - 1][c - 1])
            else:
                g[r][c] += max(g[r][c - 1], g[r - 1][c - 1], g[r + 1][c - 1])

            if c == m:
                max_gold = g[r][c] if g[r][c] >= max_gold else max_gold

    return max_gold


# print(solution())


answer = []
for _ in range(t):
    answer.append(solution())

for i in answer:
    print(i)


"""
TC -> 19\n16
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""
