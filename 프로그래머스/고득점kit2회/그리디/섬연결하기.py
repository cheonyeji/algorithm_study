# 2023-08-01 (소요시간 : 1h 30m)
# def solution(n, costs):
#     # 특정 원소가 속한 집합 찾기 (루트 노드 찾기)
#     def find_parent(parent, n):
#         if parent[n] != n:
#             # 부모 찾을 때까지 재귀적으로 호출
#             parent[n] = find_parent(parent, parent[n])
#         return parent[n]

#     # 두 원소가 속한 집합 합치기
#     def union_parent(parent, a, b):
#         a = find_parent(parent, a)
#         b = find_parent(parent, b)
#         if a < b:
#             parent[b] = a
#         else:
#             parent[a] = b

#     answer = 0
#     costs.sort(key=lambda x: x[2])  # 비용 기준으로 오름차순 정렬
#     parent = [i for i in range(n)]  # 부모 테이블, 부모를 자기 자신으로 초기화

#     for a, b, cost in costs:
#         # 사이클 존재X
#         if find_parent(parent, a) != find_parent(parent, b):
#             # 연결하고 비용 계산
#             union_parent(parent, a, b)
#             answer += cost


#     return answer
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])  # 비용 기준으로 오름차순 정렬
    connect = set([costs[0][0]])  # 연결을 확인하는 집합

    # Kruskal 알고리즘으로 최소 비용 구하기
    while len(connect) != n:
        for cost in costs:
            if cost[0] in connect and cost[1] in connect:
                continue
            if cost[0] in connect or cost[1] in connect:
                connect.update([cost[0], cost[1]])
                answer += cost[2]
                break

    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
