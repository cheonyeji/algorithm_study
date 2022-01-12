def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(
            parent, parent[x]
        )  # 루트 노드에 더 빠르게 접근 가능, 경로 압축 방법 (꼭 기억!)
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 간선 개수(v), union 수행할 개수(e)
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블

# 맨 처음에는 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합 : ", end="")
for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")

print()

# 부모 테이블 출력
print("부모 테이블 : ", end="")
for i in range(1, v + 1):
    print(parent[i], end=" ")
