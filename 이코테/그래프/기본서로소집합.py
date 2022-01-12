# find 함수가 비효율적으로 동작, 최악의 경우 find 함수가 모든 노드를 다 살펴봐야 하므로 O(v) 시간 복잡도
# 전체 시간 복잡도가 O(vm)으로 비효율적

# 특정 원소가 속한 집합 찾기 (루트 노드 찾기)
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:  # 일반적으로 더 작은 노드가 루트로 지정
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산 각각 수행
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

"""
입력예시
6 4
1 4
2 3
2 4
5 6
"""
