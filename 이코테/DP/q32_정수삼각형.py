# 2022-01-19
# 이코테 ch16 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/1932

n = int(input())

tri = []

for _ in range(n):
    tri.append(list(map(int, input().split())))


for i in range(1, n):
    for j in range(0, i + 1):
        if j == 0:
            tri[i][j] += tri[i - 1][j]
        elif j == i:
            tri[i][j] += tri[i - 1][i - 1]
        else:
            tri[i][j] += max(tri[i - 1][j - 1], tri[i - 1][j])

print(max(tri[n - 1]))

"""
TC -> 30
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""
