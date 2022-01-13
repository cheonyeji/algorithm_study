# 2022-01-13
# 이코테 ch18 그래프 이론 문제 Q44 행성 터널
# https://www.acmicpc.net/problem/2887

# 최소 비용 spanning tree

import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

edges = []

# x축 기준, y축 기준, z축 기준으로 정렬 후 정렬된 값들 사이의 간선 값만 고려해도 충분하다는 아이디어를 떠올려야 함
# x축의 간선만 사용해도 MST(최소 신장 트리)를 만들 수 있음
# 각 축 별로 가장 작은 값으로 어차피 연결할 것이므로, 정렬 후 인접한 노드 간의 값만 고려하기
x = []
y = []
z = []

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    x.append((data[0], i))  # 해당 x좌표가 몇번째 노드의 값인지 함께 저장
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

# 인접한 노드들로부터 간선 정보를 추출하여 처리
for i in range(n - 1):  # 총 n-1개의 간선만 확인하면 OK
    # cost, a, b 순서 (오름차순 정렬이므로 cost계산은 뒤 - 앞 해주면 OK)
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
"""
TC
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
"""

# 모든 간선의 경우의 수를 고려하게 되면 nC2라서 십억단위로 커져버림 -> 이렇게 싹 다 간선 정보 저장하면 XX
# def calcul_cost(x1, y1, z1, x2, y2, z2):
#     return min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))

# graph = []

# for _ in range(n):
#     graph.append(list(map(int, input().split())))

# for i in range(len(graph)):
#     for j in range(i, len(graph)):
#         if i == j:
#             continue
#         cost_ij = calcul_cost(
#             graph[i][0], graph[i][1], graph[i][2], graph[j][0], graph[j][1], graph[j][2]
#         )
#         cost_ji = calcul_cost(
#             graph[j][0], graph[j][1], graph[j][2], graph[i][0], graph[i][1], graph[i][2]
#         )
#         if cost_ji > cost_ij:
#             edges.append((cost_ij, i, j))
#         else:
#             edges.append((cost_ji, j, i))
