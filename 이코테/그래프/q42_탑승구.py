# 2022-01-13
# 이코테 ch18 그래프 이론 문제 Q42 탑승구


# 구현으로 풀었음 (출제 의도와 달랐으니 다시 풀어보자)
# g = int(input())
# p = int(input())
# graph = [[] for _ in range(g + 1)]
# answer = 0

# flag = True


# def docking(gate, airplane):
#     global answer
#     global flag
#     if gate == 0:
#         # print("더이상 도킹 불가!")
#         flag = False
#         return
#     if len(graph[gate]) == 0:
#         graph[gate].append(airplane)
#         answer += 1
#         return
#     else:
#         gate -= 1
#         docking(gate, airplane)


# for i in range(1, p + 1):
#     gate = int(input())
#     docking(gate, i)
#     if not flag:
#         break


# print("답:", end=" ")
# print(answer)

# 그래프 이론을 사용하여 풀기
# 도킹 = 탑승구 간 union 연산 수행 (해당 탑승구 root가 0이면 더이상 도킹 불가)

from typing import get_args


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


g = int(input())
p = int(input())

parent = [0] * (g + 1)
for i in range(1, g + 1):
    parent[i] = i

result = 0
for i in range(1, p + 1):
    root = find_parent(parent, int(input()))
    if root == 0:
        break
    union_parent(parent, parent, parent - 1)  # 어떤 요소들을 묶어야 하는지 파악하는 것이 중요...!
    result += 1

print(result)

# root요소에 접근해서 파악해야 한다는 것은 파악했는데, 0번 노드를 활용해서 할 생각까지 못 가서 구현으로 풀었던 문제

"""
TC 1 -> 결과 : 2
4
3
4
1
1
TC 2 -> 결과 : 4
5
4
3
3
4
4
TC 3 -> 결과 : 3
4
6
2
2
3
3
4
4 
"""
