# 2023-10-06

N, M = map(int, input().split(" "))

parent = [i for i in range(N + 1)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


edges = []

for _ in range(M):
    a, b, cost = map(int, input().split(" "))
    edges.append((cost, a, b))

edges.sort()
money = []
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        money.append(cost)

ans = sum(money) - money[-1]
print(ans)
