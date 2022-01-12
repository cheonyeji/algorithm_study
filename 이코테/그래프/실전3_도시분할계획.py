# 2022-01-12
# 이코테 ch10 그래프 이론 실전문제 3 도시 분할 계획
# https://acmicpc.net/problem/1647

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


n, m = map(int, input().split())

edges = []
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))  # c기준 정렬


# 노드가 서로 서로 연결 = 사이클 존재하는 경우에만 한 마을로 쪼갤 수 있음 -> XXX
# 마을을 쪼개고 나서 최소 비용 스패닝 트리를 고려할 게 아니라,
# 최소 비용 스패닝 트리를 일단 만들고 가장 값 큰 간선을 없애버려 집 하나를 하나의 마을로 만들어버리면 됨

edges.sort()
cost = []

for edge in edges:
    c, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        cost.append(c)

sum = 0
for i in range(len(cost) - 1):
    sum += cost[i]

print(sum)
