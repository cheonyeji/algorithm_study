# 2023-09-30
# 백준 암호 만들기 https://www.acmicpc.net/problem/1759
# 백트래킹
from sys import stdin

input = stdin.readline

L, C = map(int, input().split(" "))
data = list(input().rstrip().split(" "))
data.sort()

visited = [False for _ in range(C)]

aeiou = ["a", "e", "i", "o", "u"]

moeum = 0  # 모음
jaeum = 0  # 자음

answer = []
pick = []


def dfs(start):
    global moeum, jaeum, L
    if len(pick) == L:
        if moeum >= 1 and jaeum >= 2:
            answer.append("".join(pick))
        return

    for i in range(start, len(data)):
        if not visited[i]:
            if data[i] in aeiou:
                visited[i] = True
                moeum += 1
                pick.append(data[i])
                dfs(i)
                visited[i] = False
                pick.pop()
                moeum -= 1
            else:
                visited[i] = True
                jaeum += 1
                pick.append(data[i])
                dfs(i)
                visited[i] = False
                pick.pop()
                jaeum -= 1


dfs(0)
for a in answer:
    print(a)
