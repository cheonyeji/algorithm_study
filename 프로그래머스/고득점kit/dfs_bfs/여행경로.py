# 2023-04-17
# 프로그래머스 고득점 kit - DFS/BFS
# https://school.programmers.co.kr/learn/courses/30/lessons/43164
# 소요 시간 : 14:46 ~ 16:09 (80m) -> 테케 통과 후 50% 통과해서 해설 참고

from collections import defaultdict

# 해설 참고 코드 (많이 접근했는데 너무 꼬아서 생각해서 예외에 걸린듯!)
def solution(tickets):
    path = []

    # key - value 형태인데 시작점 : [도착점1, 도착점2] 형태로 그래프 생성
    graph = defaultdict(list)  # 리스트 형태로 딕셔너리 초기화
    for (start, end) in tickets:
        graph[start].append(end)

    # 도착점 리스트 역순 정렬 (알파벳 순으로 먼저 가기 위해)
    for v in graph.keys():
        graph[v].sort(reverse=True)

    # "ICN"부터 시작
    stack = ["ICN"]

    # dfs로 모든 노드 순회하기
    while stack:
        top = stack.pop()

        # top요소가 그래프에 없거나, top 요소를 시작점으로 하는 티켓이 없는 경우 path에 저장
        if top not in graph or not graph[top]:
            path.append(top)
        # top을 다시 스택에 넣고 top의 도착점 중 가장 마지막 지점을 꺼내와 스택에 저장(티켓 사용)
        else:
            stack.append(top)
            stack.append(graph[top].pop())

    # 방문한 순서 역순으로 반환
    return path[::-1]


# 첫번째 시도한 코드 (절반만 정답인 코드...)
def solution2(tickets):
    answer = []
    airports = []

    for case in tickets:
        depart, arrival = case
        if not depart in airports:
            airports.append(depart)
        if not arrival in airports:
            airports.append(arrival)
    airports.sort()

    graph = [[] for _ in range(len(airports))]
    maxVisit = [0 for _ in range(len(airports))]

    for case in tickets:
        depart, arrival = case
        dIdx = airports.index(depart)
        aIdx = airports.index(arrival)
        maxVisit[aIdx] += 1
        graph[dIdx].append(aIdx)

    for i in range(len(airports)):
        graph[i].sort()

    visit = [0] * len(airports)

    def dfs(vIdx, visit):
        answer.append(airports[vIdx])
        for i in graph[vIdx]:
            if visit[i] != maxVisit[i]:
                visit[i] += 1
                graph[vIdx].remove(i)
                dfs(i, visit)

    dfs(airports.index("ICN"), visit)

    return answer


print(
    solution(
        [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    )
)
# 정답 : ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
