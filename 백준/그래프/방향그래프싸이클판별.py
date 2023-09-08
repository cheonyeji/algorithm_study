# 2023-09-06
# 방향 그래프에서의 사이클 판별 (DFS 이용)

from collections import defaultdict


def solution1():
    N = 7
    # 4,6,7 노드간 사이클 존재
    edges = [(1, 2), (1, 5), (2, 3), (2, 6), (3, 4), (6, 4), (4, 7), (7, 6)]

    graph = defaultdict(list)
    for edge in edges:
        s, e = edge
        # 그래프 연결
        graph[s].append(e)

    visit = [0] * (N + 1)

    # 시간복잡도 DFS O(V+E),
    # 모든 정점에 하므로 O(v(V+E))
    def dfs(start, here):
        # 재귀 함수 종료 조건
        # 이미 방문했고
        if visit[here]:
            # 시작 정점과 현재 방문 정점이 같다면 싸이클
            if start == here:
                return False
            # 같지 않다면 싸이클X 노드에서 온 것임
            return True

        # 방문 처리
        visit[here] = True
        for node in graph[here]:
            # 시작 정점을 그대로 둔 채로 DFS로 노드 계속 탐색
            if dfs(start, node):
                # DFS가 true를 반환하는 경우 사이클 존재
                return True
            return False

    for i in range(1, N + 1):
        # 사이클이 하나라도 존재한다면 사이클이 있는 그래프
        if dfs(i, i):
            return True
        return False


print(solution1())


def solution2():
    N = 7
    # 4,6,7 노드간 사이클 존재
    edges = [(1, 2), (1, 5), (2, 3), (2, 6), (3, 4), (6, 4), (4, 7), (7, 6)]

    graph = defaultdict(list)
    for edge in edges:
        s, e = edge
        # 그래프 연결
        graph[s].append(e)

    visit = [0] * (N + 1)

    # 시간복잡도 O(V+E)로 해결하기
    # DFS를 수행하다가 재귀 탐색이 종료되지 않았는데 다시 방문하게 되면 사이클 O
    # 사이클이 존재하는 노드와 연결된 노드로부터 사이클 존재여부 바로 확인O

    def dfs2(here):
        if visit[here]:
            # DFS가 아직 안 끝났는데 사이클
            if visit[here] == -1:
                return True
            return False

        # DFS 아직 안 끝남
        visit[here] = -1

        for node in graph[here]:
            if dfs2(node):
                return True
        # DFS가 끝났으므로 1로 설정
        visit[here] = 1
        return True

    return dfs2(1)


print(solution2())
