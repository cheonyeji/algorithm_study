# 2022-01-11
# 이코테 ch17 최단 경로 문제 Q38 정확한 순위

# 자기 자신을 제외하고 모든 경로의 값이 무한이 아닌 경우 순위 계산 가능
# 모든 노드에 대해서 다른 노드와 서로 도달이 가능한지 체크

n, m = map(int, input().split())

INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1


for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = 0
for a in range(1, n + 1):
    count = 0
    for b in range(1, n + 1):
        # a->b든 b->a든 연결이 된 경우라면 count증가
        # a->b인 경우에는 a<b, b->a인 경우에는 a>b
        if graph[a][b] != INF and graph[b][a] != INF:
            count += 1

    if count == n:
        answer += 1

print(answer)

"""
테스크케이스
6 6
1 5
3 4
4 2
4 6
5 2
5 4
"""
