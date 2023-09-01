from sys import stdin

input = stdin.readline

# 노드의 개수, 간선의 개수
n, m = map(int, input().split(" "))

# 2차원 리스트를 사용하여 그래프 초기화
graph = [[int(1e9)] * (n + 1) for _ in range(n + 1)]

# 자기 자신 -> 자기 자신 비용은 0으로 초기화
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 각 간선 정보 입력받기
for _ in range(m):
    # a -> b 비용 : c
    a, b, c = map(int, input().split(" "))
    graph[a][b] = c

# 노드i -> 노드k -> 노드j 거쳐가는 것과 vs 현재거리 (i->j) 중 짧은 요소로 업데이트
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 결과 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == int(1e9):
            print("INF", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
