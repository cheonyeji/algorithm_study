# 2022-01-11
# 이코테 ch17 최단 경로 문제 Q37 플로이드
# https://www.acmicpc.net/problem/11404

n = int(input())  # 노드 수
m = int(input())  # 간선 수

INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기->자기 노드는 0으로
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 그래프 입력받아서 그리기
for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] >= c:  # 여러개의 연결 경로 중 가장 작은 값만을 저장
        graph[a][b] = c


for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
