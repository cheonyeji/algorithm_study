# 2022-01-12
# 이코테 ch10 그래프 이론 실전문제 4 커리큘럼

# 방향이 존재하는 그래프에서 방향을 유지한채 정렬 -> Topology

from collections import deque
import copy  # 리스트의 값 복제(deepcopy)를 위해

n = int(input())
# 연결 그래프
graph = [[] for _ in range(n + 1)]
# 진입차수
indegree = [0] * (n + 1)
# 강의 시간 저장
time = [0] * (n + 1)


for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    # 연결 노드로 입력이 여러개 들어오는 경우도 있으므로 리스트 슬라이싱으로 처리
    for x in data[1:-1]:
        graph[x].append(i)  # 입력받은 노드 -> i 연결
        indegree[i] += 1


def topology():
    result = copy.deepcopy(time)  # 알고리즘 수행 결과를 담는 리스트
    q = deque()

    # 진입차수 0인 노드 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])


topology()

"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""
