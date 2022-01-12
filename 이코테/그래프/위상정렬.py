# 위상정렬(Topology)
# 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 방법
# (나열 방법은 여러가지가 나올 수 있다)
# 모든 노드와 간선을 확인하므로 시간 복잡도는 O(v+e)

from collections import deque


# 노드의 개수 v, 간선의 개수 e
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for _ in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # a->b 이동 가능
    indegree[b] += 1  # 진입차수 1증가

# 위상 정렬
def topology_sort():
    result = []
    q = deque()

    # 진입차수 0인 노드 먼저 큐에 넣기
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들 진입차수 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드 큐에 넣기
            if indegree[i] == 0:
                q.append(i)
    # 위상정렬 결과 출력
    for i in result:
        print(i, end=" ")


topology_sort()

"""
입력예시
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""
