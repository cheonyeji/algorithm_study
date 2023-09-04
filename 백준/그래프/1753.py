# 2023-09-04 (소요시간 : 1h)
# 그래프 [골드4. 백준 1753 최단경로] (https://www.acmicpc.net/problem/1753)

from sys import stdin
import heapq

input = stdin.readline

V, E = map(int, input().split(" "))

# 시작정점의 번호
K = int(input())

# 그래프
graph = [[] for _ in range(V + 1)]

mydict = {}
for _ in range(E):
    u, v, w = map(int, input().split(" "))
    # 간선이 여러개일 수 있으니 최솟값만 저장하기
    mydict[(u, v)] = min(mydict.get((u, v), int(1e9)), w)

for key in mydict:
    s, e = key
    graph[s].append((e, mydict[key]))


# 최단거리 테이블
distance = [int(1e9) for _ in range(V + 1)]


# 다익스트라
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # (비용, 노드)로 힙에 값 넣기
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 최단거리 테이블을 살펴봤더니
        # 지금 길이가 더 길어서 살펴볼 필요가 없는 경우는 패스
        if distance[now] < dist:
            continue

        # 연결된 노드 살펴보기
        for i in graph[now]:
            next_node, next_node_dist = i
            cost = dist + next_node_dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))


dijkstra(K)

for i in range(1, V + 1):
    if distance[i] == int(1e9):
        print("INF")
    else:
        print(distance[i])
