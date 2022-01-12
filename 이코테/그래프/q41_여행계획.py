# 2022-01-12
# 이코테 ch18 그래프 이론 문제 Q41 여행 계획

# 입력 받은 여행 계획의 노드들이 같은 parent를 갖고 있는 경우 여행이 가능한 것
# -> 서로소 집합 알고리즘 돌려서 parent 리스트에서 판단만 해주면 될 듯

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


# 간선 수 n, 여행 계획에 속한 도시 수 m
n, m = map(int, input().split())

parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        if data[j] == 1:
            union_parent(parent, i, j + 1)

# print(parent)

plan = list(map(int, input().split()))

check = parent[plan[0]]

answer = "YES"
for i in plan:
    if check != parent[i]:
        answer = "NO"
        break

print(answer)

"""
테스트케이스
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
"""
