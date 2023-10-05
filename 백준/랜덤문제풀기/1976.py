# 2023-10-05
# 백준 여행 가자 https://www.acmicpc.net/problem/1976
# union-find 로직이 어색하여 해설 참고...

"""
문제 풀때 조건에 맞춰서 진행하는 것이 좋음
노드가 1부터 시작하면 부모 테이블도 1부터 시작하도록 셋팅하기
"""

from sys import stdin

input = stdin.readline

N = int(input())
M = int(input())

graph = [list(map(int, input().split(" "))) for _ in range(N)]

visit_plan = list(map(int, input().split(" ")))

# 자기 자신으로 부모 초기화
parent = [i for i in range(N + 1)]


# 부모 노드 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


for i in range(N):
    for j in range(N):
        # 연결된 경우 부모 노드 갱신
        if graph[i][j] == 1:
            union(i + 1, j + 1)

answer = "YES"


# 두번쨰 도시부터 첫번째 시작도시에 연결되는지만 봐주면 됨
start = parent[visit_plan[0]]
for i in range(1, M):
    if parent[visit_plan[i]] != start:
        answer = "NO"
        break
print(answer)
