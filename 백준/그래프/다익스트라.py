# 개선된 다익스트라 알고리즘

import heapq
from sys import stdin

input = stdin.readline

# 노드의 개수, 간선의 개수
n, m = map(int, input().split(" "))

# 시작 노드 번호
start = int(input())

graph = [[] for _ in range(n + 1)]

# 최단 거리 테이블 초기화
distance = [int(1e9) * (n + 1)]

# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split(" "))  # a -> b 비용 : c
    graph[a].append((b, c))  # (도착노드, 비용 순서)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # (비용, 노드). 힙은 0번째 요소를 기준으로 정렬하므로
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 이미 처리된 노드라면 넘어가기
        # 현재 경로가 더 비용이 커 처리해줄 필요 X
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 노드 보면서 최단거리 테이블 갱신
        for i in graph[now]:
            cost = dist + i[1]
            # cost가 더 작다면 업데이트
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

# 모든 노드로 가는 최단 거리 출력
for i in range(1, n + 1):
    if distance[i] == int(1e9):
        print("INF")
    else:
        print(distance[i])
