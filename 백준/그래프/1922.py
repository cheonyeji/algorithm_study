# 2023-09-06 (소요시간 : 30m)
# 그래프 [골드4. 백준 1922 네트워크 연결] (https://www.acmicpc.net/problem/1922)

from sys import stdin

input = stdin.readline

N = int(input())  # 정점
M = int(input())  # 간선

dist = []
for _ in range(M):
    a, b, c = map(int, input().split(" "))
    dist.append((a, b, c))  # a-b : 비용 c

# 간선비용 기준 정렬
dist.sort(key=lambda x: (x[2]))

parent = [i for i in range(N + 1)]


# union-find
def find_parent(parent, n):
    if parent[n] != n:
        parent[n] = find_parent(parent, parent[n])
    return parent[n]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


answer = 0
for a, b, cost in dist:
    if find_parent(parent, a) != find_parent(parent, b):
        # 사이클 X => 연결 후 최소 스패닝 트리에 포함
        union_parent(parent, a, b)
        answer += cost

print(answer)
