# 2022-01-13
# 이코테 ch18 그래프 이론 문제 Q45 최종 순위
# https://www.acmicpc.net/problem/3665

# 위상 정렬인데 이제 조금 더 고려할 점이 생긴... 고런....

from collections import deque


def solution():
    n = int(input())  # 노드 개수
    grade = list(map(int, input().split()))  # 순서대로 1등~꼴등인 팀 번호 저장 리스트
    indegree = [0] * (n + 1)  # 진입차수 저장
    # 각 노드에 연결된 간선 정보를 저장할 수 있는 인접 행렬
    graph = [[False] * (n + 1) for _ in range(n + 1)]

    # 순위가 높은 팀 -> 순위가 낮은 팀 가르키도록
    # 이렇게 하면 X
    # for g in range(len(grade)):
    #     indegree[grade[g]] = g
    #     graph[[grade[g]]].append() # 이 부분 어떻게 해야될지 있다가 고민

    # 1등부터 차례대로 입력되니까 1등->2,3,4,5등 2등->3,4,5등 이렇게 가리키도록 하면 됨
    for i in range(n):
        for j in range(i + 1, n):
            graph[grade[i]][grade[j]] = True
            indegree[grade[j]] += 1

    m = int(input())  # 방향이 바뀐 간선 수

    for _ in range(m):
        a, b = map(int, input().split())
        # 방향이 바뀌었으므로 진입차수 증감
        if graph[a][b]:  # a->b인 경우
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # 위상 정렬 시작
    q = deque()
    result = []

    # 진입차수 = 0 인 노드를 먼저 큐에 넣기
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    # 여기부터 단순히 queue에 값을 넣고 빼면서 보면 안되고
    # 1) 사이클이 발생하는지
    # 2) 위상 정렬의 결과가 여러 개가 나올 수 있는지를 체크해야 함

    onlyOne = True  # 위상 정렬의 결과가 딱 한 개만 있는지 여부
    cycle = False  # 사이클 존재 여부

    # 노드의 개수만큼만 딱 반복 (while q 아님)
    for i in range(n):
        # 1) 큐가 비어 있다 -> 사이클 발생 (사이클 안에서 빙빙 돌아서 큐가 텅 빈 것)
        if len(q) == 0:
            cycle = True
            break

        # 2) 큐의 원소가 2개 이상이면 정렬 결과가 여러 개일 수 있음
        if len(q) > 1:
            onlyOne = False
            break

        # 큐에서 원소를 꺼내며 위상 정렬 수행
        now = q.popleft()
        result.append(now)

        # 해당 원소와 연결된 노드들의 진입차수 - 1
        for j in range(1, n + 1):
            if graph[now][j]:  # graph[now]로 안하는 이유는 당연히 인접 행렬로 저장했으니까 !!
                indegree[j] -= 1

                # 진입차수가 = 0 이 되는 노드가 발생하면 큐에 넣기
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not onlyOne:
        print("?")
    else:
        for i in result:
            print(i, end=" ")
        print()


tc = int(input())

for _ in range(tc):
    solution()
