# 2022-01-13
# 이코테 ch18 그래프 이론 문제 Q43 어두운 길

# 크루스칼 알고리즘 사용 시 쉽게 해결 가능 (열심히 그래프 공부한 보람이 있다! 20분만에 솔)


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

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

edges = []
original_cost_sum = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    original_cost_sum += c
    edges.append((c, a, b))

total_cost = 0

edges.sort()
for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost

print(original_cost_sum - total_cost)
"""
TC -> 결과 : 51
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
"""
