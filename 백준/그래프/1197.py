# 2023-09-06 (소요시간 : 20m - 기본이라 알고리즘 보고 풀다)
# 그래프 [골드4. 백준 1197 최소 스패닝 트리] (https://www.acmicpc.net/problem/1197)

"""
크루스칼 알고리즘 (그리디)
1. 간선을 오름차순으로 정렬
2. 간선을 하나씩 확인하며 간선이 사이클을 발생시키는지 확인
(사이클 발생 확인 방법 : 연결된 루트 노드가 같은지)
2-1. 사이클X, 최소 스패닝 트리에 포함
(노드와 노드의 루트 노드를 연결)
2-2. 사이클O, 최소 스패닝 트리에 포함X
3. 모든 간선에 대해서 2번 과정 반복
"""
from sys import stdin

input = stdin.readline

V, E = map(int, input().split(" "))

dist = []
for _ in range(E):
    a, b, c = map(int, input().split(" "))
    dist.append([a, b, c])

# 간선을 오름차순으로 정렬
dist.sort(key=lambda x: (x[2]))

# 부모 테이블
parent = [i for i in range(V + 1)]


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
for a, b, edge in dist:
    # 사이클 존재 X
    if find_parent(parent, a) != find_parent(parent, b):
        # 연결하고 최소 스패닝 트리에 포함 (가중치만 출력하면 되므로 합계)
        union_parent(parent, a, b)
        answer += edge

print(answer)
