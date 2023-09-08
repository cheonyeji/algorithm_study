# 2023-09-06 (소요시간 : 40m 풀고 예제입력부터 이해가 안되서 풀이 참고)
# 최단거리 [골드1. 백준 16118 달빛 여우] (https://www.acmicpc.net/problem/16118)

from sys import stdin
import heapq

input = stdin.readline

# N : 정점, M : 간선
N, M = map(int, input().split(" "))

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, d = map(int, input().split(" "))
    graph[a].append((b, d * 2))
    graph[b].append((a, d * 2))

distance_fox = [int(1e9) for _ in range(N + 1)]
distance_wolf = [[int(1e9)] * 2 for _ in range(N + 1)]


def dijkstra_fox(start):
    q = []
    heapq.heappush(q, (0, start))
    distance_fox[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance_fox[now] < dist:
            continue

        for i in graph[now]:
            next_node, next_node_cost = i
            cost = dist + next_node_cost
            if distance_fox[next_node] > cost:
                distance_fox[next_node] = cost
                heapq.heappush(q, (cost, next_node))


def dijkstra_wolf(start):
    q = []
    # 빨리 도착했는지(True): distance[0], 느리게 도착했는지(False) : distance[1]
    heapq.heappush(q, (0, start, False))
    distance_wolf[start][1] = 0
    while q:
        dist, now, arrive_fast = heapq.heappop(q)

        if arrive_fast and distance_wolf[now][0] < dist:
            continue
        elif not arrive_fast and distance_wolf[now][1] < dist:
            continue

        for i in graph[now]:
            next_node, next_node_cost = i
            # 빠르게 도착했으니, 느리게 출발
            if arrive_fast:
                next_node_cost *= 2
                cost = dist + next_node_cost
                if distance_wolf[next_node][1] > cost:
                    distance_wolf[next_node][1] = cost
                    heapq.heappush(q, (cost, next_node, False))
            else:
                next_node_cost //= 2
                cost = dist + next_node_cost
                if distance_wolf[next_node][0] > cost:
                    distance_wolf[next_node][0] = cost
                    heapq.heappush(q, (cost, next_node, True))


dijkstra_fox(1)
dijkstra_wolf(1)

answer = 0
for i in range(2, N + 1):
    if distance_fox[i] < min(distance_wolf[i][0], distance_wolf[i][1]):
        answer += 1

print(answer)
