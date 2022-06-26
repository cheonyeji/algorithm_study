# 2022-06-26
# 이코테 열흘동안 뽀개기 프로젝트 3일차
# dfs bfs 실전 3 음료수 얼려 먹기
# 소요 시간 : 18:36 ~ 19:07 (30m)

# 세로 길이 n(row) 가로 길이 m(col)
n, m = map(int, input().split())

# 인접 행렬
array = []
for _ in range(n):
    array.append(list(map(int, input())))

# 상하좌우 인접한 모든 노드를 방문하면서 방문 처리
def dfs(r, c):
    # 범위 바깥
    if r < 0 or r > n - 1 or c < 0 or c > m - 1:
        return False

    # 만약 체크해볼 필요 없는 노드면 바로 탐색 stop
    if array[r][c] == 1:
        return False

    # 방문 처리
    array[r][c] = 1

    dfs(r - 1, c)
    dfs(r + 1, c)
    dfs(r, c - 1)
    dfs(r, c + 1)

    return True


answer = 0
for row in range(n):
    for col in range(m):
        if dfs(row, col) == True:
            answer += 1


print(answer)

"""
TC 1 -> 3
3 3
001
010
101

TC 2 -> 3
4 5
00110
00011
11111
00000

TC 3 -> 8
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""
