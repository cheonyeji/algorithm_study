# 2022-01-11
# 이코테 ch17 최단 경로 문제 Q40 숨바꼭질

# 시간제한 1초 입력최대값 2만으로 플로이드워셜은 사용불가

import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

start = 1
q = []
heapq.heappush(q, (0, start))
distance[start] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue

    # 현재 노드와 연결된 다른 인접한 노드를 확인
    for i in graph[now]:
        cost = dist + i[1]  # i = (목적지노드, cost)

        # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

for i in range(len(distance)):
    if distance[i] == INF:
        distance[i] = -1

# print(distance)

max_dist = max(distance)
index = distance.index(max_dist)
num = distance.count(max_dist)

print(index, max_dist, num)

"""
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
"""
