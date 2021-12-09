# 이코테 DFS/BFS : 예제 3번 음료수 얼려 먹기

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(graph, x, y):
    if graph[x][y] == 0:  # 만약 음료수가 얼 수 있다면-> 상하좌우 살펴보기
        graph[x][y] = 1  # 방문 완료

        y - 1 >= 0 and dfs(graph, x, y - 1)  # 상
        y + 1 < m and dfs(graph, x, y + 1)  # 하
        x - 1 >= 0 and dfs(graph, x - 1, y)  # 좌
        x + 1 < n and dfs(graph, x + 1, y)  # 우

        return True
    return False


icecream = 0

# 그래프 내 모든 정점을 다 살펴봐야 하므로 2중 for문 사용
for i in range(n):
    for j in range(m):
        if dfs(graph, i, j):
            icecream += 1

print(icecream)


# visited 배열 써서도 해보기

"""
테스크케이스 1, 출력예시 3
4 5
00110
00011
11111
00000

테스트케이스 2, 출력예시 8
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
