# 1번회사 -> K번 회사 -> X번 회사로 가는 최소 거리
# 입력범위가 100이하로 한정적이어 플루이드 워셜 사용 가능
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0


# 각 간선의 정보 입력받아서 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1  # 놓치지 말기. a<->b 양방향 설정

x, k = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


# 1번->K번
result = graph[1][k] + graph[k][x]

if result >= INF:
    print(-1)
else:
    print(result)
