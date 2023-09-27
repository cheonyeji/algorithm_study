# 2023-09-27 (소요시간 : 20m)
# 문제집 https://www.acmicpc.net/workbook/view/8708
# 실버4. https://www.acmicpc.net/problem/20125

"""
문제에 나온 그대로 훑으면 됨
"""

from sys import stdin

input = stdin.readline

N = int(input())

graph = []

head_found = False
head = [-1, -1]

for r in range(N):
    temp = list(input())
    if not head_found and "*" in temp:
        c = temp.index("*")
        head_found = True
        head = [r, c]
    graph.append(temp)

heart = [head[0] + 1, head[1]]

# 왼쪽 팔길이
left_arm = 0
for c in range(heart[1] - 1, -1, -1):
    if graph[heart[0]][c] == "*":
        left_arm += 1
    else:
        break

# 오른쪽 팔길이
right_arm = 0
for c in range(heart[1] + 1, N):
    if graph[heart[0]][c] == "*":
        right_arm += 1
    else:
        break

body = 0
col = heart[1]
leg_row = 0
for r in range(heart[0] + 1, N):
    if graph[r][col] == "*":
        body += 1
    else:
        leg_row = r
        break


# 다리길이
left_leg = 0
right_leg = 0
left_end = False
right_end = False

for r in range(leg_row, N):
    if left_end and right_end:
        break

    if graph[r][col - 1] == "*":
        left_leg += 1
    else:
        left_end = True

    if graph[r][col + 1] == "*":
        right_leg += 1
    else:
        right_end = True

print(heart[0] + 1, heart[1] + 1)
print(left_arm, right_arm, body, left_leg, right_leg)
