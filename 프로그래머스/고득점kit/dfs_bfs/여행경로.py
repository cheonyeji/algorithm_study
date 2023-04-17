# 2023-04-17
# 프로그래머스 고득점 kit - DFS/BFS
# https://school.programmers.co.kr/learn/courses/30/lessons/43164
# 소요 시간 : 14:46 ~ 16:09 (80m) -> 테케 통과 후 50% 통과해서 해설 참고

# 첫번째 시도한 코드 (절반만 정답인 코드...)
def solution(tickets):
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
