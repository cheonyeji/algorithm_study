# 2022-01-12
# 이코테 ch10 그래프 이론 실전문제 2 팀 결성

# 팀 합치기 연산 -> union
# 같은 팀 여부 확인 -> 루트 노드 확인


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

for _ in range(m):
    x, a, b = map(int, input().split())
    if x == 1:
        # 같은 팀 여부 확인
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
    else:
        # 팀 합치기
        union_parent(parent, a, b)

"""
테스트케이스
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""
