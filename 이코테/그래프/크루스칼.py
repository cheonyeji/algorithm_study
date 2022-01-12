# 크루스칼 알고리즘 : 가장 적은 비용으로 모든 노드를 연결하는 알고리즘 (최소 비용 스패닝 트리)
# 총
# O(ElogE)의 시간복잡도 -> sort의 시간복잡도 (서로소 집합 알고리즘 복잡도는 정렬보다 작아서 무시)


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


v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

# 모든 간선을 담을 리스트
edges = []
# 최종 비용을 담을 변수
result = 0

# 모든 간선에 대한 정보 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순 정렬을 위해 첫번째 원소를 cost로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

"""
입력 예시
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
"""
